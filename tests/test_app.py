import json
import unittest

from flask import Flask, request
from app import app


class TestApp(unittest.TestCase):

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
            "name": "Movit",
            "Category": "Cosmetics",
            "Quantity added to cart": "4boxes",
            "unit price": "shs 96,000",
            "Created by": "mbabazi"

        }

    def test_can_add_product(self):
        response = self.client.post(
            "/api/v1/products", data=json.dumps(self.good_product), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_can_get_products(self):
        response = self.client.get('/api/v1/products')
        self.assertEqual(response.status_code, 200)

    def test_delete_product(self):
        response = self.client.delete("/api/v1/products/1")
        self.assertEqual(response.status_code, 200)

    def test_can_add_sale_order(self):
        response = self.client.post("/api/v1/sales", data=json.dumps(self.sale_order), content_type="application/JSON")
        self.assertEqual(response.status_code, 201)

    def test_can_get_sales(self):
        response = self.client.get('/api/v1/sales')
        self.assertEqual(response.status_code, 200)

    def test_cannot_get_non_existing(self):
        response = self.client.get('/api/v1/sales/again')
        self.assertEqual(response.status_code, 404)

    def test_invalid_JSON(self):
        response = self.client.post('/api/v1/products/1',
                                    data="not a json",
                                    content_type='application/json')
        self.assertEqual(response.status_code, 405)

    def test_cannot_delete_non_existent(self):
        response = self.client.delete("/api/v1/products/6")
        self.assertEqual(response.status_code, 404)
