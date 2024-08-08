from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Article, Comment, Like


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    """
    Customizes the Django admin interface for the Article model.
    """
    list_display = ('title', 'author', 'created_on', 'status',)
    list_filter = ('status', 'created_on', 'author')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content', 'excerpt',)


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    """
    Customizes the Django admin interface for the Comment model.
    """
    list_display = ('author', 'article', 'created_on', 'approved')
    list_filter = ('author', 'created_on', 'approved')


# Registration of Like model
admin.site.register(Like)
