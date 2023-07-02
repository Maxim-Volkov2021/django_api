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
from .search_logic import *

# Create your views here.
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.filter(archive=False).order_by('-id')
    serializer_class = NewsSerializer
    permission_classes = (IsOwnerOrReadOnly,)


    @action(methods=['get'], detail=False)
    def search(self, request, *args, **kwargs):
        if "query" in request.GET:
            query = search_with_AND_OR(request, param="news")
            if query == None:
                return JsonResponse({'detail': "Bad Request"}, status=400)
            self.queryset = News.objects.filter(query, archive=False).order_by('-id')
            return viewsets.ModelViewSet.list(self, request, *args, **kwargs)
        else:
            return JsonResponse({'detail': "Bad Request"}, status=400)

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

    @action(methods=['get'], detail=False)
    def tags_search(self, request, *args, **kwargs):
        if "query" in request.GET:
            query = search_with_AND_OR(request, param="tags")
            if query == None:
                return JsonResponse({'detail': "Bad Request"}, status=400)
            self.serializer_class = TagsSerializer
            self.queryset = Tags.objects.filter(query).order_by('-id')
            return viewsets.ModelViewSet.list(self, request, *args, **kwargs)
        else:
            return JsonResponse({'detail': "Bad Request"}, status=400)


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
    def authors_search(self, request, *args, **kwargs):
        if "query" in request.GET:
            query = search_with_AND_OR(request, param="authors")
            if query == None:
                return JsonResponse({'detail': "Bad Request"}, status=400)
            self.serializer_class = AuthorsSerializer
            self.queryset = Author.objects.filter(query).order_by('-id')
            return viewsets.ModelViewSet.list(self, request, *args, **kwargs)
        else:
            return JsonResponse({'detail': "Bad Request"}, status=400)


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


class NewNotAuthorViewSet(mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   GenericViewSet):

    queryset = NewsNotAuthor.objects.all().order_by('-id')
    serializer_class = NewsNotAuthorSerializer
    permission_classes = (IsOwnerOrReadOnlyForNotAuthor,)
    def destroy(self, request, *args, **kwargs):
        if "lamp" in request.data and request.data["lamp"]:
            news = NewsNotAuthor.objects.filter(pk=kwargs["pk"])
            if len(news) > 0:

                #create author
                context = {
                    "user": news[0].user.pk,
                    "name": news[0].nameAuthor
                }
                self.serializer_class = AuthorsAdminSerializer
                self.queryset = Author.objects.all()
                serializer = self.get_serializer(data=context)
                serializer.is_valid(raise_exception=True)
                idAuthor = serializer.save()

                # create news
                context = {
                    "title": news[0].title,
                    "content": news[0].content,
                    "tags": [i['id'] for i in news[0].tags.all().values("id")],
                    "author": idAuthor.pk
                }
                self.serializer_class = NewsSerializer
                self.queryset = News.objects.all()
                serializer = self.get_serializer(data=context)
                serializer.is_valid(raise_exception=True)
                serializer.save()

                #delete news in news not author
                return viewsets.ModelViewSet.destroy(self, request, *args, **kwargs)
            else:
                return JsonResponse({'detail': "Not found news."}, status=404)

        return viewsets.ModelViewSet.destroy(self, request, *args, **kwargs)


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
