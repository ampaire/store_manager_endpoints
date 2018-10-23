from flask import Flask, jsonify, request
import datetime
app = Flask(__name__)

Sale_orders = [
    {
        'date': '21-10-2018',
        'Name': 'Geisha',
        'Category': 'Cosmetics',
        'Quantity added to cart': '2 boxes',
        'Unit price': 'shs 96,000',
        'Created by' : 'mbabazi'
    },
    {
        'date': '21-10-2018',
        'Name': 'Pampers Pants',
        'Category': 'Diapers',
        'Quantity added to cart': '4 packets',
        'Unit price': 'shs 20,000',
        'Created by' : 'namara'

    }
]


@app.route("/",)
def index():
    return 'Add products to the shopping cart'


@app.route("/api/v1/Sale_orders", methods=["POST"])
def add_order():

    for sale_order in Sale_orders:

        if not request.json:
            return('Invalid input format'),404

        sale_order = {

            'date': datetime.datetime.today(),
            "Name": request.json['Name'],
            "Category": request.json.get("Category", ""),
            "Quantity added to cart": request.json['Quantity added to cart'],
            "Unit price": request.json["Unit price"],
            "Created by" : request.json["Created by"]
        }

    Sale_orders.append(sale_order)
    if len(sale_order) == 0:
        return ("Cannot add order with missing data")
    return jsonify({'Sale_orders': Sale_orders}), 200


if __name__ == "__main__":
    app.run(debug=True, port=8080)
