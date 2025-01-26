from dj_rest_auth.serializers import LoginSerializer

class CustomLoginSerializer(LoginSerializer):
    username = None

# Исправление ошибки. При попытке залогиниться предлагалось 3 поля ввода: username, email, password. Я решил что
# логиниться пользователи будут с лишь с помощью email и password. Вот и закастомил встроенный функционал библиотеки
# dj_rest_auth