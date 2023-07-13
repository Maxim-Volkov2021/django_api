from rest_framework import permissions

from .models import Author, User, NewsNotAuthor


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user and request.user.is_staff:
            return True
        elif request.method == 'POST' and (request.user and request.user.is_authenticated):
            author = Author.objects.filter(user=request.user).order_by('id')
            if len(author) > 0:
                request.data['author'] = author[0].pk
                return True
        elif request.method == 'PUT' or request.method == 'PATCH':
            return True
        return False


    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user and request.user.is_staff:
            return True
        elif obj.author == None or obj.author.user == None:
            return False

        return bool(obj.author.user == request.user)


class IsOwnerOrReadOnlyForNotAuthor(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_staff:
            return True
        elif request.method == 'POST' and (request.user and request.user.is_authenticated):
            news = NewsNotAuthor.objects.filter(user=request.user)
            if len(Author.objects.filter(user=request.user).order_by('id')) == 0 and len(news) == 0:
                request.data['user'] = request.user.pk
                return True
        return False
    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_staff:
            return True
        if request.method in permissions.SAFE_METHODS and (request.user and request.user.is_staff):
            return True