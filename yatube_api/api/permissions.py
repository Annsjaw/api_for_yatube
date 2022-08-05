from rest_framework import permissions


class ReadOnly(permissions.BasePermission):

    message = 'Создание и редактирование групп через API - ЗАПРЕЩЕНО!'

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS