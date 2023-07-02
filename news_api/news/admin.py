from django.contrib import admin

from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_author_name', 'timeCreate', 'archive')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'author__name', 'author__user__username', 'author__user__first_name', 'author__user__last_name')
    list_filter = ('tags', 'author', 'timeCreate')
    list_editable = ('archive',)
    filter_horizontal = ('tags',)

    def get_author_name(self, object):
        if object.author:
            if object.author.user.first_name or object.author.user.last_name:
                return object.author.user.first_name + " " + object.author.user.last_name
            else:
                return object.author.user.username

    get_author_name.short_description = "author"


class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_author_name', 'get_author_username', 'name')
    list_display_links = ('id', 'get_author_name', 'get_author_username', 'name')
    search_fields = ('user__first_name', 'user__last_name', 'user__username')

    def get_author_name(self, object):
        if object.user:
            if object.user.first_name or object.user.last_name:
                return object.user.first_name + " " + object.user.last_name
    get_author_name.short_description = "name"

    def get_author_username(self, object):
        if object.user:
            if object.user.username:
                return object.user.username
    get_author_username.short_description = "username"


class NewsNotAuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_user_username', 'nameAuthor', 'timeCreate')
    list_display_links = ('id', 'title')
    search_fields = (
    'title',
    'content',
    'nameAuthor',
    'user__username',
    'user__first_name',
    'user__last_name'
    )
    list_filter = ('tags', 'user', 'timeCreate')
    filter_horizontal = ('tags',)

    def get_user_username(self, object):
        if object.user:
            if object.user.username:
                return object.user.username
    get_user_username.short_description = "username"


admin.site.register(News, NewsAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Author, AuthorsAdmin)
admin.site.register(NewsNotAuthor, NewsNotAuthorAdmin)

