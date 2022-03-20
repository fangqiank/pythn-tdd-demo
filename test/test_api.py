import json
import unittest
from flask import request
from app import app


class TestApi(unittest.TestCase):
    def test_ner_endpoint_given_json_body_returns_200(self):
        with app.test_client() as client:
            res = client.post('/ner', json={'sentence': 'hello world'})
            assert res.status_code == 200

    def Test_ner_endpoint_given_json_body_with_known_entities_returns_entity_result_in_response(self):
        with app.test_client() as client:
            res = client.post('/ner', json={'sentence': 'Barack Obama'})
            data = json.loads(res.get_data())
            assert data['entities'][0]['ent'] == 'Barack Obama'
            assert data['entities'][0]['label'] == 'Person'