from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import Article

class TestArticleViews(TestCase):
    
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
        article_data = {
            'content': 'Test comment!',
        }
        response = self.client.post(reverse(
            'article_detail', args=['article-title']), article_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Your comment was submitted successfully and awaits approval.",
            response.content
        )
        
