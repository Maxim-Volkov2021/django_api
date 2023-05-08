from rest_framework import generics, viewsets
from rest_framework import mixins
from django.http import QueryDict
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import *
from .serializers import *


# Create your views here.
def checkingAdminOrAuthor(request):
    if request.user.is_superuser:
        return True
    elif request.user.is_authenticated:
        try:
            author = Author.objects.filter(user__username=request.user.username).order_by('id')[0]
            request.data['author'] = author.pk
            return True
        except:
            # print("not author")
            data = {"detail": "You are not the author."}
            return [data, 403]
    else:
        # print("not authorized")
        data = {"detail": "You are not authorized."}
        return [data, 401]
# class NewsApiListCreate(generics.ListCreateAPIView):
#     queryset = News.objects.order_by("-timeCreate").filter(archive=False)
#     serializer_class = NewsSerializer
#
#     def post(self, request, *args, **kwargs):
#         check = checkingAdminOrAuthor(request)
#         if check == True:
#             return self.create(request, *args, **kwargs)
#         else:
#             return Response(check)
#
#
# class NewsApiRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer
#
#     def put(self, request, *args, **kwargs):
#         check = checkingAdminOrAuthor(request)
#         if check == True:
#             return self.update(request, *args, **kwargs)
#         else:
#             return Response(check)
#
#
#     def patch(self, request, *args, **kwargs):
#         check = checkingAdminOrAuthor(request)
#         if check == True:
#             return self.partial_update(request, *args, **kwargs)
#         else:
#             return Response(check)
#
#
#     def delete(self, request, *args, **kwargs):
#         check = checkingAdminOrAuthor(request)
#         if check == True:
#             return self.destroy(request, *args, **kwargs)
#         else:
#             return Response(check)

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    @action(methods=['get'], detail=True)
    def tag(self, request, pk):
        tag = Tags.objects.filter(pk=pk)
        if tag[0]:
            return Response({'tag': tag[0].name})
        else:
            return Response({'detail': "Tag not found."}, 404)


    @action(methods=['get'], detail=False)
    def tags(self, request):
        tags = Tags.objects.all()
        return Response({'tags': [{"id": t.pk, "name": t.name} for t in tags]})


    @action(methods=['get'], detail=True)
    def author(self, request, pk):
        author = Author.objects.filter(pk=pk)
        if author[0]:
            return Response({'author': author[0].name})
        else:
            return Response({'detail': "Author not found."}, 404)

    @action(methods=['get'], detail=False)
    def authors(self, request):
        authors = Author.objects.all()
        return Response({'authors': [{"id": a.pk, "name": a.name} for a in authors]})


    def create(self, request, *args, **kwargs):
        check = checkingAdminOrAuthor(request)
        if check == True:
            return self.create(request, *args, **kwargs)
        else:
            return Response(check[0], check[1])


    def update(self, request, *args, **kwargs):
        check = checkingAdminOrAuthor(request)
        if check == True:
            return self.update(request, *args, **kwargs)
        else:
            return Response(check[0], check[1])


    def partial_update(self, request, *args, **kwargs):
        check = checkingAdminOrAuthor(request)
        if check == True:
            return self.partial_update(request, *args, **kwargs)
        else:
            return Response(check[0], check[1])


    def destroy(self, request, *args, **kwargs):
        check = checkingAdminOrAuthor(request)
        if check == True:
            return self.destroy(request, *args, **kwargs)
        else:
            return Response(check[0], check[1])
