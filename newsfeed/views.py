from django.shortcuts import render
from django.views import generic
from .models import Article

# Create your views here.
class ArticleList(generic.ListView):
    queryset = Article.objects.filter(status=1)
    template_name = "newsfeed/index.html"