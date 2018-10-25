import json
import unittest

from flask import Flask, request
from __init__ import app


class TestAdd(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client(self)
        self.client.testing = True

        self.good_product = {
            "name": "Sunseed",
            "suppliers": "Mukwano ltd",
            "Category": "Cooking oil",
            "unit price": "shs 30,000"

        }
        self.bad_product = {
            "name": "Geisha",
            "suppliers": "Product of African Queen ltd",
            "Category": "Cosmetics",
            "unit price": "shs 96,000"

        }
        self.sale_order = {

        }

    def test_can_add_product(self):
        response = self.client.post("/api/v1/products", data=json.dumps(self.good_product), content_type='application/json')
        self.assertEqual(response.status_code, 201)
    def test_delete(self):
        response = self.client.delete("/api/v1/products/1")
        self.assertEqual(response.status_code, 200)
        
    def test_cannot_delete_non_existent(self):
        response = self.client.delete("/api/v1/products/3")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
