from rest_framework import generics, viewsets
from rest_framework import mixins
from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import *
from .serializers import *
from .permissions import *


# Create your views here.
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)


    @action(methods=['get'], detail=True)
    def tag(self, request, pk):
        tag = Tags.objects.filter(pk=pk)
        if tag[0]:
            return JsonResponse({'tag': [{"id": tag[0].pk, "name": tag[0].name}]})
        else:
            return JsonResponse({'detail': "Tag not found."}, 404)


    @action(methods=['get'], detail=False)
    def tags(self, request):
        tags = Tags.objects.all()
        return JsonResponse({'tags': [{"id": t.pk, "name": t.name} for t in tags]})


    @action(methods=['get'], detail=True)
    def author(self, request, pk):
        author = Author.objects.filter(pk=pk)
        if author[0]:
            return JsonResponse({'author': [{"id": author[0].pk, "name": author[0].name}]})
        else:
            return JsonResponse({'detail': "Author not found."}, 404)

    @action(methods=['get'], detail=False)
    def authors(self, request):
        authors = Author.objects.all()
        return JsonResponse({'authors': [{"id": a.pk, "name": a.name} for a in authors]})


class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(
                user,
               context=self.get_serializer_context()
            ).data,
            "message": "User Created Successfully. Now perform Login to get your token",
        })


class AccountApi(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)


    def get(self, request, *args, **kwargs):
        context = {"account": {
            "username": request.user.username,
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "email": request.user.email,
            "is_author": False
        }}
        author = Author.objects.filter(user__username=request.user.username).order_by('id')
        try:
            context["account"]["author_id"] = author[0].pk
            context["account"]["author_name"] = author[0].name
            context["account"]["is_author"] = True
        except:
            pass
        return JsonResponse(context)


def PageNotFound(request, exception):
    return JsonResponse({'detail': "Page not found!"}, status=404)
