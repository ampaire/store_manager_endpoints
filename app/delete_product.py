from flask import Flask, jsonify, request, abort
from datetime import date
app = Flask(__name__)


products = [
    {
        'date': '22-10-2018',
        'Name': 'Sunseed cooking oil',
        'Suppliers': 'Mukwano Industries ltd',
        'Category': 'Coooking oil',
        'Quantity supplied': '4 boxes',
        'Unit price': 'shs 96,000'
    },
    {
        'date': '22-10-2018',
        'Name': 'Blue band',
        'Suppliers': 'Mukwano Industries ltd',
        'Category': 'Margerine',
        'Quantity supplied': '3 boxes',
        'Unit price': 'shs 97,000'

    }
]


@app.route("/",)
def index():
    return ('This is your products page')


@app.route("/api/v1/products/<Name>", methods=["DELETE"])
def delete_product(Name):
    product = [product for product in products if product['Name'] == Name]
    if len(product) == 0:
        return ("Cannot delete non-existent item"), 404
    products.remove(product[0])
    return jsonify({'result': 'Deleted'}), 200


if __name__ == "__main__":
    app.run(debug=True, port=8080)
