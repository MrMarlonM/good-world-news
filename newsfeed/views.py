from django.shortcuts import render
from django.views import generic
from .models import Article

# Create your views here.
def article_list(request):
    breaking_news = Article.objects.filter(is_breaking_news=True, status=1).order_by('-created_on')
    articles = Article.objects.filter(is_breaking_news=False, status=1).order_by('-created_on')
    context = {
        'breaking_news': breaking_news,
        'articles': articles,
    }
    return render(request, 'newsfeed/index.html', context)