from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Article
from .forms import CommentForm

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
    comments = article.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)

            new_comment.author = request.user
            new_comment.article = article
            new_comment.save()
            
            return redirect('article_detail', slug=slug)
    else:
        comment_form = CommentForm() 

    context = {
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(
        request,
        "newsfeed/article_detail.html",
        context,
    )

def about(request):
    return render(request, 'newsfeed/about.html')