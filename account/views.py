from dj_rest_auth.views import LogoutView
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from .models import CustomUser
from rest_framework import permissions, generics
from . import serializers


class UserViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = CustomUser.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.UserListSerializer
        return serializers.UserDetailSerializer


# Now we need to create view, that registers the user
class UserRegisterView(generics.CreateAPIView):
    serializer_class = serializers.UserRegisterSerializer

# Это кастомизатор для модуля logout. Мы просто устанавливаем пермишенсы
class CastomLogoutView(LogoutView):
    permission_classes = (permissions.IsAuthenticated,)