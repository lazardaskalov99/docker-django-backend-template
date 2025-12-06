from django.test import TestCase, Client
from django.urls import reverse


class PingEndpointTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_ping_endpoint(self):
        response = self.client.get(reverse('ping'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong', response.content.decode())