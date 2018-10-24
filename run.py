from app.add_product import app
from app.create_order import app
from app.get_oneproduct import app
from app.get_products import app
from app.get_sale_orders import app
from app.delete_product import app
from app.modify_product import app

if __name__ == "__main__":
    app.run(debug=True, port=8080)
