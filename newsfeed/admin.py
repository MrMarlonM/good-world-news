from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Article, Comment, Like


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content', 'excerpt',)


# Register your models here.
admin.site.register(Comment)
admin.site.register(Like)