from rest_framework import permissions

class IsDoctor(permissions.BasePermission):
    """
    Разрешение, которое разрешает доступ только пользователям с ролью 'doctor'.
    """

    def has_permission(self, request, view):
        # Проверяем, что пользователь аутентифицирован и его роль == 'doctor'
        return request.user.is_authenticated and request.user.role == 'doctor'
