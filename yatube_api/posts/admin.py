from django.contrib import admin
from posts.models import Comment, Group, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'group')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'

class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'text', 'created')


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Comment, CommentAdmin)
