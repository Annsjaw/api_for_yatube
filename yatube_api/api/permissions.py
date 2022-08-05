from rest_framework import permissions


class ReadOnly(permissions.BasePermission):
    """Исключительно GET запрос."""

    message = 'Создание и редактирование групп через API - ЗАПРЕЩЕНО!'

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class AuthorOrReadOnly(permissions.BasePermission):
    """Доступ по GET всем, создание поста только авторизованному юзеру,
    редактирование только автору."""

    message = 'Изменение чужого контента запрещено!'

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
