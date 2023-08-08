from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request

from rest_app.models import Product


class AdminOrReadOnly(BasePermission):

    def has_permission(self, request: Request, view):
        if request.method in ['PUT', 'DELETE', 'POST']:
            return request.user and request.user.is_staff
        return True
