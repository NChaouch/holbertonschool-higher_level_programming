from flask import Flask, render_template, request
import csv
import json

app = Flask(__name__)


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
    if source not in ['json', 'csv']:
        message = "Wrong source"
        return render_template('product_display.html',
                               products=products, message=message)

    # Lire/charger les données en fonction de la source
    try:
        if source == 'json':
            # charger les données en lecture depuis le fichier JSON
            with open('products.json', 'r') as file:
                products = json.load(file)

        elif source == 'csv':
            # charger les données en lecture depuis le fichier CSV
            with open('products.csv', 'r') as file:
                # lire les données sous forme de dictionnaire
                reader = csv.DictReader(file)
                products = [row for row in reader]

        if product_id:
            products = [product for product in products if str(
                product['id']) == product_id]

            if not products:
                message = (f"Product not found.")

    # Faire la gestion des erreurs si le fichier est introuvable
    except FileNotFoundError:
        message = (f"File not found.")

    except Exception as e:
        message = (f"An error occurred: {e}")

    # Retourner le rendu du template avec les produits ou le message d'erreur
    return render_template('product_display.html',
                           products=products, message=message)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
