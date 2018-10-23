from flask import Flask, jsonify, request
import datetime
app = Flask(__name__)

products = [
    {
        'date': '19-10-2018',
        'Name': 'Geisha',
        'Suppliers': 'Product of African Queen ltd',
        'Category': 'Cosmetics',
        'Quantity supplied': '65 boxes',
        'Unit price': 'shs 96,000'
    },
    {
        'date': '19-10-2018',
        'Name': 'Pampers Pants',
        'Suppliers': 'Product of African Queen ltd',
        'Category': 'Diapers',
        'Quantity supplied': '68 packets',
        'Unit price': 'shs 20,000'

    }
]


@app.route("/")
def index():
    return 'Restricted to the admin only'


@app.route("/api/v1/products", methods=["POST"])
def add_product():

    for product in products:

        if not request.json:
            return ('Invalid input format'),404       

        product = {

            'date': datetime.datetime.today(),
            "Name": request.json['Name'],
            "Suppliers": request.json.get("Suppliers", ""),
            "Category": request.json.get("Category", ""),
            "Quantity supplied": request.json['Quantity supplied'],
            "Unit price": request.json["Unit price"]
        }

    products.append(product)
    if len(product) == 0:
        return ("Cannot add empty sett"),405
    return jsonify({'products': products}),200


if __name__ == "__main__":
    app.run(debug=True, port=8080)
