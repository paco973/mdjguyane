
from django.contrib import admin
from django.db import models
from django.forms import Textarea
from django_summernote.admin import SummernoteModelAdmin

from blog.models import PostCategory, Post, Comment


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']




class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'author_name',
        'title',
        'category',
        'published',
        'comments_count',
    )

    list_filter = (
        'category__name',
        'published',
    )

    autocomplete_fields = ['category']

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 90})},
    }

    def comments_count(self, obj):
        return Comment.objects.filter(post=obj).count()
    comments_count.short_description = 'Comments'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    search_fields = ['post__title', 'author_name', ]
    list_display = (
        'post',
        'author_name',
        'status',
        'moderation_text',

        'text',
    )

    list_editable = ('status', 'moderation_text', )

    list_filter = ('status', )