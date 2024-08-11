from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import Article, Comment

class TestArticleViews(TestCase):
    """All tests for the article_detail view"""
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.article = Article(
            title="Article Title",
            slug="article-title",
            author=self.user,
            is_breaking_news=True,
            excerpt="Article Excerpt",
            content="Article Content",
            status=1,
            )
        self.article.save()
    
    def test_render_article_detail_page_with_comment_form(self):
        """
        Test if the article_detail page is rendered correctly
        with a Comment form
        """
        response = self.client.get(reverse(
            'article_detail', args=['article-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Article Title", response.content)
        self.assertIn(b"Article Content", response.content)
        self.assertIsInstance(
            response.context['comment_form'], CommentForm
        )
    
    def test_successful_comment_submission(self):
        "Test for adding a comment as registered user"
        self.client.login(
            username="myUsername",
            password="myPassword"
        )
        comment_data = {
            'content': 'Test comment!',
        }
        response = self.client.post(reverse(
            'article_detail', args=['article-title']), comment_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Your comment was submitted successfully and awaits approval.",
            response.content
        )
        new_comment = Comment.objects.latest('id')
        self.assertFalse(new_comment.approved)


class TestEditCommentView(TestCase):
    """Test for the comment_edit view"""
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')

        self.article = Article(
            title="Article Title",
            slug="article-title",
            author=self.user,
            is_breaking_news=True,
            excerpt="Article Excerpt",
            content="Article Content",
            status=1,
            )
        self.article.save()

        self.comment = Comment.objects.create(
            article=self.article, author=self.user, content='Original comment')
        self.comment.save()

        self.client.login(
            username='testuser', password='testpassword'
        )
    
    def test_successful_comment_edit(self):
        """Checks if a comment is edited and updated correctly"""
        updated_comment_data = {
            'content': 'Updated comment'
        }

        response = self.client.post(
            reverse('comment_edit', args=[self.article.slug, self.comment.id]),
            updated_comment_data,
            follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(
            response, reverse('article_detail', args=[self.article.slug])
        )
        self.assertIn(
            b"Your comment was updated successfully and awaits approval now",
            response.content
        )
        updated_comment = Comment.objects.get(pk=self.comment.id)
        self.assertEqual(updated_comment.content, 'Updated comment')
        self.assertFalse(updated_comment.approved)
    
def TestDeleteCommentView(TestCase):
    """All tests for the comment_delete view"""
    def setUp(self):
        self.user = User.objects.create_user(
        username='testuser', password='testpassword')

        self.article = Article(
            title="Article Title",
            slug="article-title",
            author=self.user,
            is_breaking_news=True,
            excerpt="Article Excerpt",
            content="Article Content",
            status=1,
            )
        self.article.save()

        self.comment = Comment.objects.create(
            article=self.article,
            author=self.user,
            content='Original comment'
                )
        self.comment.save()

        self.client.login(
            username='testuser', password='testpassword'
            )
        
    def test_successful_comment_delete(self):
        """Checks if user can delete a comment successfully"""
        response = self.client.post(
            reverse(
                'comment_delete',
                args=[self.article.slug, self.comment.id])
            )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse('article_detail', args=[self.article.slug])
            )
        self.assertIn(
            b"Your comment was successfully deleted.",
            response.content
        )
        with self.assertRaises(Comment.DoesNotExist):
            Comment.objects.get(pk=self.comment.id)