
from project.tests.base import BaseTestCase
import json


class TestFilterCRUDAPI(BaseTestCase):

    def test_valid_encode_request(self):

        with self.client:
            response = self.client.post('v1/encode',
                                        data=json.dumps({
                                            'sentence': 'Ulam was great mathematician!'
                                        }),
                                        content_type='application/json')
        self.assert200(response)

    def test_too_short_encode_request(self):
        with self.client:
            response = self.client.post('v1/encode',
                                        data=json.dumps({
                                            'sentence': 'Foo'
                                        }),
                                        content_type='application/json')
        self.assert400(response)
        data = json.loads(response.data)
        self.assertEqual(
            data['message'],
            'Sentence is too short to be encoded!')

    def test_no_json_encode_request(self):
        with self.client:
            response = self.client.post('v1/encode')
        self.assert400(response)
        data = json.loads(response.data)
        self.assertEqual(
            data['message'],
            'Provide {"sentence":"<str>"} in payload!')

    def test_valid_decode_request(self):

        with self.client:
            response = self.client.post('v1/decode',
                                        data=json.dumps({
                                            "sentence": "Ulam was great mathematician!"
                                        }),
                                        content_type='application/json')
        self.assert200(response)

    def test_too_short_decode_request(self):
        with self.client:
            response = self.client.post('v1/decode',
                                        data=json.dumps({
                                            'sentence': 'Foo'
                                        }),
                                        content_type='application/json')
        self.assert400(response)
        data = json.loads(response.data)
        self.assertEqual(
            data['message'],
            'Sentence is too short to be encoded!')

    def test_no_json_decode_request(self):
        with self.client:
            response = self.client.post('v1/decode')
        self.assert400(response)
        data = json.loads(response.data)
        self.assertEqual(
            data['message'],
            'Provide {"sentence":"<str>"} in payload!')
