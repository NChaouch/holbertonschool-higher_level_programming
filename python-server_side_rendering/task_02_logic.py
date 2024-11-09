from flask import Flask, render_template
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
            item = data.get("items")
            return render_template('items.html', item)
    except:
        return render_template('items.html', item)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
