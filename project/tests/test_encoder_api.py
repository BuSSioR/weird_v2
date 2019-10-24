
from project.tests.base import BaseTestCase
import json


class TestFilterCRUDAPI(BaseTestCase):

    def test_valid_encode_request(self):
        '''Tests correct encode case'''
        with self.client:
            response = self.client.post('v1/encode',
                                        data=json.dumps({
                                            'sentence': 'Ulam was great mathematician!'
                                        }),
                                        content_type='application/json')
        self.assert200(response)

    def test_too_short_encode_request(self):
        '''Tests too short sentence case'''
        with self.client:
            response = self.client.post('v1/encode',
                                        data=json.dumps({
                                            'sentence': 'Foo'
                                        }),
                                        content_type='application/json')
        self.assert400(response)

    def test_no_json_encode_request(self):
        '''Test missing payload case'''
        with self.client:
            response = self.client.post('v1/encode')
        self.assert400(response)

    def test_valid_decode_without_list_request(self):
        '''Test valid case of decoding by program alghoritm'''
        with self.client:
            response = self.client.post('v1/decode_without_list',
                                        data=json.dumps({
                                            "sentence": "Ulam was great mathematician!"
                                        }),
                                        content_type='application/json')
        self.assert200(response)

    def test_too_short_decode_without_list_request(self):
        '''Tests too short sentence decoding case'''
        with self.client:
            response = self.client.post('v1/decode_without_list',
                                        data=json.dumps({
                                            'sentence': 'Foo'
                                        }),
                                        content_type='application/json')
        self.assert400(response)

    def test_no_json_decode_without_list_request(self):
        '''Tests empty payload decode case'''
        with self.client:
            response = self.client.post('v1/decode_without_list')
        self.assert400(response)

    def test_valid_decode(self):
        '''Tests valid decode with list case'''
        with self.client:
            response = self.client.post('v1/decode',
                                        data=json.dumps({
                                            "sentence": "Ualm was gerat matheamtiican!",
                                            "decode_list": ['Ulam','was','great','mathematician']
                                        }),
                                        content_type='application/json')
        self.assert200(response)

    def test_no_json_decode(self):
        '''Tests empty payload decode with list case'''
        with self.client:
            response = self.client.post('v1/decode')
        self.assert400(response)

    def test_missing_words_in_list_decode(self):
        '''Tests too short word list case.'''
        with self.client:
            response = self.client.post('v1/decode',
                                        data=json.dumps({
                                            "sentence": "Ualm was gerat matheamtiican!",
                                            "decode_list": ['Ulam','was','great']
                                        }),
                                        content_type='application/json')
        self.assert400(response)    
    
    def test_no_list_decode(self):
        '''Tests invalida payload decode case: list missing'''
        with self.client:
            response = self.client.post('v1/decode',
                                        data=json.dumps({
                                            "sentence": "Ualm was gerat matheamtiican!",
                                        }),
                                        content_type='application/json')
        self.assert400(response)