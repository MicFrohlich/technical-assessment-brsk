from django.test import TestCase
import requests
from requests_mock import mock

class MyAPITestCase(TestCase):
    def test_my_endpoint(self):
        # Mocking the API call
        with mock() as m:
            data = {"sentence": "test sentence"}
            m.post('http://localhost:8000/api/replace-words/', json=data, status_code=200)

            # Make a request to the Django API endpoint
            response = self.client.post('/api/replace-words/', data=data, content_type='application/json')
            
            # Assert the response status code and content
            self.assertEqual(response.status_code, 200)
            self.assertNotEqual(response.json()["new_sentence"], data["sentence"])

    def test_random_response(self):
        # Make sequential POST requests to the API endpoint and ensure responses are not the same
        responses = []
        for _ in range(5):  # Change the number of requests as needed
            response = self.client.post('/api/replace-words/', data='{"sentence": "test sentence"}', content_type='application/json')
            responses.append(response.json())
        
        # Check if any response is the same as the first one
        self.assertFalse(all(response == responses[0] for response in responses), "Error: Responses are not random")
