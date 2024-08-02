from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from .models import Article, Comment, Like
from .forms import CommentForm

# Create your views here.
def article_list(request):
    """
    view to show newsfeed on homepage
    """
    breaking_news = Article.objects.filter(is_breaking_news=True, status=1).order_by('-created_on')
    articles = Article.objects.filter(is_breaking_news=False, status=1).order_by('-created_on')
    context = {
        'breaking_news': breaking_news,
        'articles': articles,
    }
    return render(request, 'newsfeed/index.html', context)


def article_detail(request, slug):
    """
    view to show individual article on page
    """
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
        'user': request.user,
        'number_of_likes': article.number_of_likes(),
    }

    return render(
        request,
        "newsfeed/article_detail.html",
        context,
    )

def about(request):
    return render(request, 'newsfeed/about.html')


def comment_edit(request, slug, comment_id):
    """
    View to edit comments
    """
    if request.method == "POST":
        articles = Article.objects.filter(status=1)
        article = get_object_or_404(articles, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.approved = False
            comment.save()
    
    return HttpResponseRedirect(reverse('article_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comments
    """
    articles = Article.objects.filter(status=1)
    article = get_object_or_404(articles, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()

    return HttpResponseRedirect(reverse('article_detail', args=[slug]))


@login_required
def article_like(request, slug):
    """
    handles liking/unliking of articles
    """
    articles = Article.objects.filter(status=1)
    article = get_object_or_404(articles, slug=slug)
    existing_like = Like.objects.filter(user=request.user, content_type=ContentType.objects.get_for_model(Article), object_id=article.id).first()

    if existing_like:
        existing_like.delete()
    else:
        Like.objects.create(user=request.user, content_object=article)
    
    return HttpResponseRedirect(reverse('article_detail', args=[slug]))