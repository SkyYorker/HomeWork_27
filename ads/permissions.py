from rest_framework import permissions

from user.models import UserRoles


class IsOwnerOrAdminOrModerator(permissions.BasePermission):
    message = "У вас нет прав"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author or request.user.role in [UserRoles.MODERATOR, UserRoles.ADMIN]:
            return True
        return False
