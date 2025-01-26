from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class LoginTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="testuser@gmail.com", password="password123", role='doctor',
        )
        self.token = Token.objects.create(user=self.user)

    def test_login(self):
        # Send a POST request to /account/login/ endpoint
        response = self.client.post(
            '/account/login/',
            {'email': "testuser@gmail.com", 'password': "password123"},
            format='json'
        )
        # Assert that the response has status code 200
        self.assertEqual(response.status_code, 200)
        # Assert that the response contains a token
        self.assertIn('key', response.data)
