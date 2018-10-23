import unittest
from flask import Flask
import json

from app.modify_product import app

print(app)


class Testmodifies(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_modifies_product(self):
        response = self.client.put("/api/v1/products/1", data=json.dumps({
            "name": "Sunrise",
            "Suppliers": "Mukwano Industries ltd",
            "Category": "Coooking oil",
            "unit price": "shs.60,000"
        }), content_type='application/JSON')
        self.assertEqual(response.status_code, 200)

    def test_assert_200(self):
        response = self.client.put("/api/v1/products/1",
                                   data=json.dumps(
                                       {
                                           "name": "Sunrise",
                                           "Suppliers": "Mukwano Industries ltd",
                                           "Category": "Coooking oil",
                                           "unit price": "shs.60,000"
                                       }
                                    ),
                                   content_type='application/JSON')
        self.assertEqual(response.status_code, 200)

    def test_cannot_modifies_nonexisting_item(self):

        response = self.client.get('/api/v1/products/4')
        self.assertEqual(response.status_code, 405)

    def test_invalid_JSON(self):
        response = self.client.post('/api/v1/products/1',
                                    data="not a json",
                                    content_type='application/json')
        self.assertEqual(response.status_code, 405)


if __name__ == '__main__':
    unittest.main()
