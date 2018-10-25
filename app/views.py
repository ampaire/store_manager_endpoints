from flask import Flask, jsonify, request
from __init__ import app
import datetime


products = [
    {
        "id_": 1,
        "date": "19-10-2018",
        "name": "Geisha",
        "suppliers": "Product of African Queen ltd",
        "Category": "Cosmetics",
        "unit price": "shs 96,000"
    },
    {
        "id_": 2,
        "date": "19-10-2018",
        "name": "Pampers Pants",
        "suppliers": "Product of African Queen ltd",
        "Category": "Diapers",
        "unit price": "shs 20,000"

    }
]
sale_orders = [
    {
        "id_": 1,
        "date": "21-10-2018",
        "name": "Movit",
        "Category": "Cosmetics",
        "Quantity added to cart": "2 boxes",
        "unit price": "shs 96,000",
        "Created by": "mbabazi"
    },
    {
        "id_": 2,
        "date": "21-10-2018",
        "name": "Dettol",
        "Category": "Cosmetics",
        "Quantity added to cart": "4 packets",
        "unit price": "shs 20,000",
        "Created by": "namara"

    }
]


@app.route("/")
def index():
    return "Welcome to your Store! Happy browsing."


@app.route("/api/v1/products", methods=["GET"])
def get_products():

    return jsonify({"products": products})

@app.route("/api/v1/products", methods=["POST"])
def create_product():

    data = {
        "id": products[-1][id_]+1,
        "date": datetime.datetime.today(),
        "name": request.json["name"],
        "suppliers": request.json.get("suppliers", ""),
        "Category": request.json.get("Category", ""),
        "unit price": request.json["unit price"]
    }
    product= json.get("data")
    products.append(product)
    if not request.json:
        return ("Invalid input format"), 404
    if product in products:
        return ("Oops! Product already exists"), 400
    if len(product) == 0:
        return ("Cannot add empty product"), 405
    return jsonify({"products": products}), 201


@app.route("/api/v1/products/<int:id_>", methods=["GET"])
def get_one_product(id_):
    product = [product for product in products if product["id_"] == id_]
    if len(product) == 0:
        return("Cannot find requested item. Try checking the spelling and try again"), 404
    return jsonify({"product": product})


@app.route("/api/v1/products/<int:id_>", methods=["PUT"])
def modify_a_product(name):
    product = [product for product in products if product["id_"] == id_]
    product[0]["name"] = request.json.get("name", product[0]["name"])
    product[0]["suppliers"] = request.json.get(
        "suppliers", product[0]["suppliers"])
    product[0]["Category"] = request.json.get(
        "Category", product[0]["Category"])
    product[0]["unit price"] = request.json.get(
        "unit price", product[0]["unit price"])

    return jsonify({"products": products})


@app.route("/api/v1/products/<int:id_>", methods=["DELETE"])
def delete_product(id_):
    product = [product for product in products if product['id_'] == id_]
    if len(product) == 0:
        return ("Failed to Delete! Cannot delete non-existent item"), 404
    products.remove(product[0])
    return jsonify({'result': 'Successfully Deleted'}), 200


@app.route("/api/v1/sale_orders", methods=["POST"])
def add_sale_order():
    sale_order = {

        "date": datetime.datetime.today(),
        "name": request.json["name"],
        "Quantity added to cart": request.json.get("Quantity added to cart", ""),
        "Category": request.json.get("Category", ""),
        "Created by": request.json["Created by"],
        "unit price": request.json["unit price"]
    }
    return jsonify({"sale_order": sale_order}), 200

@app.route("/api/v1/sale_orders", methods=["GET"]
def get_sale_orders():
    return jsonify({"sale_orders": sale_orders})


if __name__ == "__main__":
    app.run(debug=True, port="8080")
