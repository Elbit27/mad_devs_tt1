from django.test import TestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model


class TestPatient(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="testuser@gmail.com", password="password123", role='doctor',
        )
        self.token = Token.objects.create(user=self.user)

    def test_listing(self):
        response = self.client.get(
            '/patients/',
            HTTP_AUTHORIZATION='Token ' + self.token.key
        )
        self.assertEqual(response.status_code, 200)

    def test_non_doctor_cannot_access_patients(self):
        # Изменяем роль пользователя
        self.user.role = "patient"
        self.user.save()

        # Устанавливаем токен в заголовок Authorization
        response = self.client.get(
            '/patients/',
            HTTP_AUTHORIZATION = 'Token ' + self.token.key

        )

        # Проверяем, что доступ запрещен
        self.assertEqual(response.status_code, 403)  # Forbidden