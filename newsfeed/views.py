from django.shortcuts import render, get_object_or_404
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

def article_detail(request, slug):
    articles = Article.objects.filter(status=1)
    article = get_object_or_404(articles, slug=slug)

    return render(
        request,
        "newsfeed/article_detail.html",
        {"article": article},
    )

def about(request):
    return render(request, 'newsfeed/about.html')