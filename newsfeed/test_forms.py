from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):
    
    def test_form_is_valid(self):
        comment_form = CommentForm({'content': 'Great Post!'})
        self.assertTrue(comment_form.is_valid())

    def test_form_is_invalid(self):
        comment_form = CommentForm({'content': ''})
        self.assertFalse(comment_form.is_valid())