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
    return 'Products in the shopping cart'


@app.route("/api/v1/Sale_orders", methods=["GET"])
def get_sale_orders():

    return jsonify({'Sale_orders': Sale_orders}), 200


if __name__ == "__main__":
    app.run(debug=True, port=8080)
