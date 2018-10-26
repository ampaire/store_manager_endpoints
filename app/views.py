from flask import Flask, jsonify, request
from app.__init__ import app
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
    product = {
        "id_": products[-1]["id_"]+1,
        "date": datetime.datetime.today(),
        "name": request.get_json()["name"],
        "suppliers": request.get_json().get("suppliers"),
        "Category": request.get_json().get("Category"),
        "unit price": request.get_json().get("unit price")
    }
    if product in products:
        return ("Oops! Product already exists"), 400
    products.append(product)
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
def modify_a_product(id_):
    product = [product for product in products if product["id_"] == id_]
    product[0]["name"] = request.get_json().get("name")
    product[0]["suppliers"] = request.get_json().get("suppliers")
    product[0]["Category"] = request.get_json().get("Category")
    product[0]["unit price"] = request.get_json().get("unit price")

    if product not in products:
        return("item not found!"),404

    return jsonify({"products": products})


@app.route("/api/v1/products/<int:id_>", methods=["DELETE"])
def delete_product(id_):
    product = [product for product in products if product['id_'] == id_]
    if len(product) == 0:
        return ("Failed to Delete! Cannot delete non-existent item"), 404
    products.remove(product[0])
    return jsonify({'products':products, "message": 'Successfully Deleted'}), 200


@app.route("/api/v1/sales", methods=["POST"])
def add_sale_order():
    sale_order = {
        "id_": sale_orders[-1]["id_"]+1,
        "date": datetime.datetime.today(),
        "name": request.get_json()["name"],
        "suppliers": request.get_json().get("suppliers", ""),
        "Category": request.get_json().get("Category", ""),
        "unit price": request.get_json()["unit price"]
    }
    if sale_order in sale_orders:
        return ("Oops! sale_order already exists"), 400
    sale_orders.append(sale_order)
    if len(sale_order) == 0:
        return ("You have not added any sale_order"), 404
    return jsonify({"sale_orders": sale_orders}), 201

    if sale_order in sale_orders:
        return ("Oops! sale_order already exists"), 400
    sale_orders.append(sale_order)
    if len(sale_order) == 0:
        return ("You have not created any sale order"), 405
    return jsonify({"sale_orders": sale_orders}), 201

@app.route("/api/v1/sales", methods=["GET"])
def get_sale_orders():
    return jsonify({"sale_orders": sale_orders})

