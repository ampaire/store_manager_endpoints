from flask import Flask, jsonify, request
app = Flask(__name__)
import datetime


products = [
    {
        'date': '19-10-2018',
        'Name': 'Colgate',
        'Suppliers': 'Product of African Queen ltd',
        'Category': 'Cosmetics',
        'Quantity supplied': '85 boxes',
        'Unit price': 'shs 48,000'

    },
    {
        'date': '19-10-2018',
        'Name': 'Blue band',
        'Suppliers': 'Mukwano Industries limited',
        'Category': 'Margerine',
        'Quantity supplied': '30 boxes',
        'Unit price': 'shs 96,000'
    }
]


@app.route("/",)
def index():
    return 'Welcome to the products page'


@app.route("/api/v1/products", methods=["GET"])
def get_products():

    return jsonify({'products': products})


if __name__ == "__main__":
    app.run(debug=True, port=8080)
