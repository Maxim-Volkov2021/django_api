from rest_framework import generics, viewsets
from rest_framework import mixins
from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.db.models import Q

from .models import *
from .serializers import *
from .permissions import *

# Create your views here.
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.filter(archive=False)
    serializer_class = NewsSerializer
    permission_classes = (IsOwnerOrReadOnly,)


    def character_definition_for_query(self, text):
        #list_math_method = ["=", "~"]
        list_name = ["title", "content", "author__id", 'author__name', 'author__user__first_name', 'author__user__last_name', "tags__id", "tags__name"]
        result = None
        if "=" in text:
            name_and_value = text.split("=")
            name_and_value[0] = name_and_value[0].replace(".", "__")
            if len(name_and_value) == 2 and name_and_value[0] in list_name:
                temp = {name_and_value[0]: name_and_value[1]}
                result = Q(**temp)
        if "~" in text:
            name_and_value = text.split("~")
            name_and_value[0] = name_and_value[0].replace(".", "__")
            if len(name_and_value) == 2 and name_and_value[0] in list_name:
                temp = {name_and_value[0] + "__contains": name_and_value[1]}
                result = Q(**temp)
        return result


    def list(self, request, *args, **kwargs):
        if "query" in request.GET:
            text_query = request.GET["query"]
            symbol_AND = " AND "
            symbol_OR = " OR "
            AND_query = None
            OR_query = None
            query = None

            if symbol_AND in text_query:
                AND_list = text_query.split(symbol_AND)
                AND_query_list = []
                for i in range(len(AND_list)):
                    if symbol_OR in AND_list[i]:
                        OR_list = AND_list[i].split(symbol_OR)
                        OR_query_list = []

                        for j in range(len(OR_list)):
                            OR_query_list.append(self.character_definition_for_query(OR_list[j]))
                            if OR_query_list[len(OR_query_list) - 1] != None and OR_query == None:
                                OR_query = OR_query_list[len(OR_query_list) - 1]
                            elif OR_query_list[len(OR_query_list) - 1] != None:
                                OR_query.add(OR_query_list[len(OR_query_list) - 1], Q.OR)

                        if AND_query == None and OR_query != None:
                            AND_query = OR_query
                        elif AND_query != None and OR_query != None:
                            AND_query.add(OR_query, Q.AND)

                        OR_query = None


                    else:
                        AND_query_list.append(self.character_definition_for_query(AND_list[i]))
                        if AND_query_list[len(AND_query_list) - 1] != None and AND_query == None:
                            AND_query = AND_query_list[len(AND_query_list) - 1]
                        elif AND_query_list[len(AND_query_list) - 1] != None:
                            AND_query.add(AND_query_list[len(AND_query_list) - 1], Q.AND)

                    if (len(AND_list) - 1) == i:
                        query = AND_query

            elif symbol_OR in text_query:
                OR_list = text_query.split(symbol_OR)
                OR_query_list = []
                for j in range(len(OR_list)):
                    OR_query_list.append(self.character_definition_for_query(OR_list[j]))
                    if OR_query_list[len(OR_query_list) - 1] != None and OR_query == None:
                        OR_query = OR_query_list[len(OR_query_list) - 1]
                    elif OR_query_list[len(OR_query_list) - 1] != None:
                        OR_query.add(OR_query_list[len(OR_query_list) - 1], Q.OR)
                query = OR_query
            else:
                query = self.character_definition_for_query(text_query)

            self.queryset = News.objects.filter(query)

        return viewsets.ModelViewSet.list(self, request, *args, **kwargs)


    def update(self, request, *args, **kwargs):
        self.queryset = News.objects.all()
        return viewsets.ModelViewSet.update(self, request, *args, **kwargs)


    @action(methods=['get'], detail=True)
    def tag(self, request, pk, *args, **kwargs):
        tag = Tags.objects.filter(pk=pk)
        if len(tag) > 0:
            self.queryset = tag
            self.serializer_class = TagsSerializer
            return viewsets.ModelViewSet.list(self, request, *args, **kwargs)
        else:
            return JsonResponse({'detail': "Tag not found."}, status=404)


    @action(methods=['get'], detail=False)
    def tags(self, request, *args, **kwargs):
        self.queryset = Tags.objects.all()
        self.serializer_class = TagsSerializer
        return viewsets.ModelViewSet.list(self, request, *args, **kwargs)


    @action(methods=['get'], detail=True)
    def author(self, request, pk, *args, **kwargs):
        author = Author.objects.filter(pk=pk)
        if len(author) > 0:
            self.queryset = author
            self.serializer_class = AuthorsSerializer
            return viewsets.ModelViewSet.list(self, request, *args, **kwargs)
        else:
            return JsonResponse({'detail': "Author not found."}, status=404)

    @action(methods=['get'], detail=False)
    def authors(self, request, *args, **kwargs):
        self.queryset = Author.objects.all()
        self.serializer_class = AuthorsSerializer
        return viewsets.ModelViewSet.list(self, request, *args, **kwargs)

    @action(methods=['get'], detail=False)
    def my(self, request, *args, **kwargs):
        if request.user and request.user.is_authenticated:
            author = Author.objects.filter(user=request.user)
            if len(author) > 0:
                news = News.objects.filter(author=author[0])
                if len(news) > 0:
                    self.queryset = news
                    return viewsets.ModelViewSet.list(self, request, *args, **kwargs)
                else:
                    return JsonResponse({'detail': "Not found news."}, status=204)
            else:
                return JsonResponse({'detail': "You are not the author."}, status=403)
        else:
            return JsonResponse({'detail': "You not authorized."}, status=401)


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
