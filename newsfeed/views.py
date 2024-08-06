from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.contenttypes.models import ContentType
from .models import Article, Comment, Like
from .forms import CommentForm


def article_list(request):
    """
    Renders the homepage (newsfeed) with a list of articles.

    Retrieves:
    - The latest breaking news article (if any) with 'is_breaking_news' set to True and 'status' set to 1 (published), ordered by descending creation date.
    - All other published articles (with 'is_breaking_news' set to False and 'status' set to 1), ordered by descending creation date.

    Context:
    - `breaking_news`: The latest breaking news article or None if there isn't one.
    - `articles`: A queryset of all other published articles.

    Template:
    - Renders the 'newsfeed/index.html' template.
    """
    breaking_news = Article.objects.filter(is_breaking_news=True, status=1).order_by('-created_on')
    articles = Article.objects.filter(is_breaking_news=False, status=1).order_by('-created_on')

    liked_article_ids = list(Like.objects.filter(user=request.user, content_type=ContentType.objects.get_for_model(Article)).values_list('object_id', flat=True))

    context = {
        'breaking_news': breaking_news,
        'articles': articles,
        'liked_article_ids': liked_article_ids,
    }
    return render(request, 'newsfeed/index.html', context)


def article_detail(request, slug):
    """
    Renders the detail page for a single article.

    Retrieves:
    - The article object based on the provided slug, ensuring it's published (status=1).
    - All comments associated with the article.

    Handles:
    - GET requests: Displays the article details, existing comments, and a comment form.
    - POST requests: Processes comment form submissions, creates a new comment, associates it 
                      with the article and the logged-in user, and saves it to the database. 
                      Then redirects back to the article detail page with a success message.

    Context:
    - `article`: The Article object being viewed.
    - `comments`: A queryset of all comments associated with the article.
    - `comment_form`: An instance of the CommentForm for submitting new comments.
    - `user`: The currently logged-in user.
    - `number_of_likes`: The number of likes for the article.
    - `is_moderator`: A boolean indicating whether the current user is a moderator.

    Template:
    - Renders the 'newsfeed/article_detail.html' template.
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
            
            messages.add_message(
                request, messages.SUCCESS,
                'Your comment was submitted successfully and awaits aproval now.'
            )
    
    comment_form = CommentForm() 

    context = {
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
        'user': request.user,
        'number_of_likes': article.number_of_likes(),
        'is_moderator': request.user.groups.filter(name='Moderator').exists(),
        'existing_like': Like.objects.filter(user=request.user, content_type=ContentType.objects.get_for_model(Article), object_id=article.id).first()
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
    Handles editing an existing comment.

    Retrieves:
    - The published article based on the provided slug.
    - The comment object to be edited based on the comment_id.

    Handles:
    - POST requests: Processes the comment edit form submission.
        - If the form is valid and the user is either the comment author or a moderator:
            - Updates the comment with the new data from the form.
            - Sets the comment's 'approved' status to False (awaiting approval).
            - Saves the updated comment.
            - Redirects to the article detail page with a success message.
        - If the form is invalid or the user is not authorized:
            - Redirects to the article detail page with an error message.

    - GET requests: (Assumed but not explicitly handled in the code)
        - Would likely render a form for editing the comment (not implemented in the current code).

    Arguments:
    - slug: The slug of the article the comment belongs to.
    - comment_id: The ID of the comment to be edited.

    Returns:
    - HttpResponseRedirect: Redirects to the article detail page after processing the request.
    """
    if request.method == "POST":
        articles = Article.objects.filter(status=1)
        article = get_object_or_404(articles, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and (comment.author == request.user
        or request.user.groups.filter(name='Moderator').exists()):
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.approved = False
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your comment was updated successfully and awaits approval now'
                )
        else:
            messages.add_message(
                request, messages.ERROR,
                'Something went wrong, please make sure you are logged in and try again.'
                )

    return HttpResponseRedirect(reverse('article_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Handles the deletion of a comment.

    Retrieves:
    - The published article based on the provided slug.
    - The comment object to be deleted based on the comment_id.

    Handles:
    - If the user is the comment author or a moderator:
        - Deletes the comment.
        - Adds a success message to the request.
    - Otherwise (user is not authorized):
        - Adds an error message to the request.

    Arguments:
    - slug: The slug of the article the comment belongs to.
    - comment_id: The ID of the comment to be deleted.

    Returns:
    - HttpResponseRedirect: Redirects to the article detail page after processing the request.
    """
    articles = Article.objects.filter(status=1)
    article = get_object_or_404(articles, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if (comment.author == request.user or
    request.user.groups.filter(name='Moderator').exists()):
        comment.delete()
        messages.add_message(
            request, messages.SUCCESS,
            'Your comment was successfully deleted.'
            )
    else:
        messages.add_message(
            request, messages.ERROR,
            'Something went wrong, please make sure you are logged in and try again.'
        )

    return HttpResponseRedirect(reverse('article_detail', args=[slug]))


@login_required
def article_like(request, slug):
    """
    Handles liking/unliking of articles.

    Retrieves:
    - The published article based on the provided slug.

    Handles:
    - Checks if the user has already liked the article.
    - If the user has liked the article:
        - Deletes the existing like.
        - Adds a success message indicating the article was unliked.
    - If the user has not liked the article:
        - Creates a new like object, associating the user with the article.
        - Adds a success message indicating the article was liked.

    Arguments:
    - slug: The slug of the article to be liked/unliked.

    Returns:
    - HttpResponseRedirect: Redirects back to the referring page.
    """
    articles = Article.objects.filter(status=1)
    article = get_object_or_404(articles, slug=slug)
    existing_like = Like.objects.filter(user=request.user, content_type=ContentType.objects.get_for_model(Article), object_id=article.id).first()

    if existing_like:
        existing_like.delete()
        messages.add_message(
            request, messages.SUCCESS,
            'You unliked the article successfully.'
        )
    else:
        Like.objects.create(user=request.user, content_object=article)
        messages.add_message(
            request, messages.SUCCESS,
            'You liked the article successfully.'
        )
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
@user_passes_test(lambda u: u.groups.filter(name='Moderator').exists())
def approve_comment(request, slug, comment_id):
    """
    Approves a comment, making it visible on the article detail page.

    Retrieves:
    - The comment object to be approved based on the comment_id.

    Handles:
    - Sets the comment's 'approved' status to True.
    - Saves the updated comment.
    - Adds a success message to the request.

    Arguments:
    - slug: The slug of the article the comment belongs to (not directly used in the current implementation).
    - comment_id: The ID of the comment to be approved.

    Returns:
    - HttpResponseRedirect: Redirects to the article detail page after processing the request.

    Permissions:
    - Requires the user to be logged in and belong to the 'Moderator' group.
    """
    comment = get_object_or_404(Comment, id=comment_id)
    comment.approved = True
    comment.save()
    messages.add_message(
        request, messages.SUCCESS,
        'Approval was successful!'
    )
    return redirect('article_detail', slug=comment.article.slug) 