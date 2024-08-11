from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):
    """All tests for the comment form"""
    def test_form_is_valid(self):
        """Test to check the comment form is valid"""
        comment_form = CommentForm({'content': 'Great Post!'})
        self.assertTrue(comment_form.is_valid())

    def test_form_is_invalid(self):
        """Test if comment form is correctly invalid"""
        comment_form = CommentForm({'content': ''})
        self.assertFalse(comment_form.is_valid())
