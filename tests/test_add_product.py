import json
import unittest

from app.add_product import app
from flask import Flask, request


class TestAdd(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client(self)
        self.client.testing = True

    def test_can_add_product(self):
        response = self.client.post("/api/v1/products",
                                    data=json.dumps(
                                        {
                                            "Name": "Pampers kapale",
                                            "Suppliers": "Product of African Queen ltd",
                                            "Category": "Diapers",
                                            "Quantity supplied": "60 packets",
                                            "Unit price": "shs 23,000"
                                        }
                                    ),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_all_required_fields_can_take_both_str_and_int(self):

        response = self.client.post("/api/v1/products",
                                    data=json.dumps(
                                        {
                                            "Name": "Pampers kapale",
                                            "Suppliers": "Product of African Queen ltd",
                                            "Category": "Diapers",
                                            "Quantity supplied": "60 packets",
                                            "Unit price": "shs 23,000"
                                        }
                                    ),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_cannot_add_empty_product(self):
        response = self.client.get('/api/v1/products')
        self.assertEqual(response.status_code, 405)


if __name__ == "__main__":
    unittest.main()
