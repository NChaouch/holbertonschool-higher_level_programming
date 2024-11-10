from flask import Flask, render_template, request
import csv
import json
import sqlite3

"""
import for code
"""

app = Flask(__name__)

"""
code
"""


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    try:
        with open('items.json', "r") as file_open:
            data = json.load(file_open)
            items = data.get("items", [])
            return render_template('items.html', items=items)
    except Exception as e:
        return render_template('items.html', items=[])


@app.route('/products', methods=['GET'])
def display_products():
    # Récupérer les paramètres de la requête
    source = request.args.get('source', '')
    product_id = request.args.get('id', None)
    message = None
    products = None

    # Vérifier si le paramètre 'source' est valide
    if source not in ['json', 'csv', 'sql']:
        message = "Wrong source"
        return render_template('product_display.html',
                               products=products, message=message)

    # Lire/charger les données en fonction de la source
    try:
        if source == 'json':
            # Charger les données en lecture depuis le fichier JSON
            with open('products.json', 'r') as file:
                products = json.load(file)

        elif source == 'csv':
            # Charger les données en lecture depuis le fichier CSV
            with open('products.csv', 'r') as file:
                # Lire les données sous forme de dico
                reader = csv.DictReader(file)
                products = [row for row in reader]

        elif source == 'sql':
            # Connexion bd SQLite
            conn = sqlite3.connect('products.db')
            cursor = conn.cursor()
            query = (f"SELECT id, name, category, price FROM Products")

            # faire un filtre si un 'product_id' est là
            if product_id:
                print(f"Executing query: SELECT * FROM Products
                      WHERE id={product_id}")
                query = (f"SELECT id, name, category, price FROM
                         Products WHERE id=?")
                cursor.execute(query, (product_id,))
            else:
                cursor.execute(query)

            # Récupérer toutes les lignes puis fermer la connexion
            rows = cursor.fetchall()
            conn.close()

            # Transformer les données en une liste de dico
            products = [
                {'id': row[0], 'name': row[1],
                 'category': row[2], 'price': row[3]}
                for row in rows
            ]

        # Filtrer les produits si un 'product_id' est est là
        if product_id and source in ['json', 'csv']:
            products = [product for product in products if str(product['id']
                                                               ) == product_id]
            if not products:
                message = (f"Product not found.")

    except FileNotFoundError:
        message = (f"File not found.")

    except sqlite3.Error as e:
        message = (f"Database error: {e}")

    except Exception as e:
        message = (f"An error occurred: {e}")

    # Retourner le rendu du template avec les produits ou le message d'erreur
    return render_template('product_display.html',
                           products=products, message=message)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
