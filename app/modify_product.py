from flask import Flask, jsonify, request, abort
from datetime import date
app = Flask(__name__)


products = [
    {
        "id_": 1,
        "date": "22-10-2018",
        "name": "Sunseed",
        "Suppliers": "Mukwano Industries ltd",
        "Category": "Coooking oil",
        "unit price": "shs, 98,000",

    },
    {
        "id_":2,
        "date": "22-10-2018",
        "name": "Blueband",
        "Suppliers": "Mukwano Industries ltd",
        "Category": "Margerine",
        "unit price": "shs, 98,000"

    }
]


@app.route("/")
def index():
    return ("This is your products page")


@app.route("/api/v1/products/<int:id_>", methods=["PUT"])
def modify_product(id_):
    product = [product for product in products if product["id_"] == id_]
    product[0]["name"] = request.json.get("name", product[0]["name"])
    product[0]["Suppliers"] = request.json.get("Suppliers", product[0]["Suppliers"])
    product[0]["Category"] = request.json.get("Category", product[0]["Category"])
    product[0]["unit price"] = request.json.get("unit price",product[0]["unit price"])

    return jsonify({"products": product[0]}), 200


if __name__ == "__main__":
    app.run(debug=True, port="8080")
