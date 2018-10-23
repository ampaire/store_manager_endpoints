import json
import unittest

from app.create_order import app
from flask import Flask, request


class TestCreateOrder(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client(self)
        self.client.testing = True

    def test_can_add_Sale_order(self):
        response = self.client.post('/api/v1/Sale_orders',
                                    data=json.dumps(
                                        {
                                            'Name': 'Magic washing powder',
                                            'Category': 'Detergents',
                                            'Quantity added to cart': '7 boxes',
                                            'Unit price': 'shs 45,000',
                                            'Created by': 'kl'
                                        }
                                    ),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_all_required_fields_can_take_both_str_and_int(self):

        response = self.client.post('/api/v1/Sale_orders',
                                    data=json.dumps(
                                        {
                                            'Name': 'Magic washing powder',
                                            'Category': 'Detergents',
                                            'Quantity added to cart': 7,
                                            'Unit price': 'shs 45,000',
                                            'Created by': 'kl'
                                        }
                                    ),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_cannot_add_nonJSON(self):
        response = self.client.post('/api/v1/Sale_orders',
                                    data="This is a string! It's not JSON!")
        self.assertEqual(response.status_code, 404)

    def test_cannot_add_empty_Sale_order(self):
        response = self.client.get('/api/v1/Sale_orders')
        self.assertEqual(response.status_code, 405)


if __name__ == '__main__':
    unittest.main()
