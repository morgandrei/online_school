from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsModerator(BasePermission):
    message = 'Вы не являетесь модератором'

    def has_permission(self, request, view):
        if request.user.role == UserRoles.MODERATOR:
            return True
        return False


class IsOwner(BasePermission):
    message = 'Вы не являетесь владельцем'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False


class IsMember(BasePermission):
    message = 'Вы не являетесь участником проекта'

    def has_permission(self, request, view):
        return request.user.role == UserRoles.MEMBER


class IsSuperuser(BasePermission):
    message = 'Вы не являетесь администратором'

    def has_object_permission(self, request, view, obj):
        if request.user == request.user.is_superuser:
            return True
        return False
