from rest_framework import generics, viewsets
from rest_framework import mixins
from django.http import QueryDict
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import *
from .serializers import *
from .permissions import *


# Create your views here.
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    @action(methods=['get'], detail=True)
    def tag(self, request, pk):
        tag = Tags.objects.filter(pk=pk)
        if tag[0]:
            return Response({'tag': [{"id": tag[0].pk, "name": tag[0].name}]})
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
            return Response({'author': [{"id": author[0].pk, "name": author[0].name}]})
        else:
            return Response({'detail': "Author not found."}, 404)

    @action(methods=['get'], detail=False)
    def authors(self, request):
        authors = Author.objects.all()
        return Response({'authors': [{"id": a.pk, "name": a.name} for a in authors]})
