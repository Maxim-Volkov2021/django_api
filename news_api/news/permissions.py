from rest_framework import permissions

from news.models import Author


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == 'POST' and (request.user and request.user.is_authenticated):
            author = Author.objects.filter(user=request.user).order_by('id')
            if author[0]:
                request.data['author'] = author[0].pk
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