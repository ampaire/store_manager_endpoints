from flask import Flask, jsonify, request, abort
app = Flask(__name__)

products = [
    {
        'date': '19-10-2018',
        'name': 'Dettol',
        'Suppliers': 'Product of African Queen ltd',
        'Category': 'Cosmetics',
        'Quantity supplied': '20 boxes',
        'Unit price': 'shs 96,000'
    },
    {
        'date': '19-10-2018',
        'name': 'Coke soda',
        'Suppliers': 'Century bottling company ltd',
        'Category': "Beverages",
        'Quantity supplied': '25 cartons',
        'Unit price': 'shs 12,000'
    }
]


@app.route("/")
def index():
    return "Here is your product"


@app.route("/api/v1/products/<name>", methods=["GET"])
def getEntry(name):
    product = [product for product in products if product["name"] == name]
    if len(product) == 0:
        abort(404)
    return jsonify({'product': product})


if __name__ == "__main__":
    app.run(debug=True, port=8080)
