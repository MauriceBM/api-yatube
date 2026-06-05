from django.contrib import admin

from .models import Comment, Group, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'text', 'pub_date', 'author', 'group'
    )
    search_fields = ('text',)
    list_filter = ('pub_date', 'author')
    list_editable = ('group',)
    empty_value_display = '-пусто-'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug')
    search_fields = ('title', 'slug')
    list_filter = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    empty_value_display = '-пусто-'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'text', 'author', 'post', 'created'
    )
    search_fields = ('text', 'author__username')
    list_filter = ('created', 'author')
    list_editable = ('post',)
    empty_value_display = '-пусто-'
