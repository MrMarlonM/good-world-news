from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):
    
    def test_form_is_valid(self):
        """Checks if the form is valid"""
        form = ContactForm({
            'name': 'tester',
            'email': 'test@test.com',
            'reason': 'question',
            'message': 'testing the form!'
        })
        self.assertTrue(
            form.is_valid(),
            msg="Form is not valid!"
        )

    def test_name_is_required(self):
        """Test for the 'name' field"""
        form = ContactForm({
            'name': '',
            'email': 'test@test.com',
            'reason': 'question',
            'message': 'test'
        })
        self.assertFalse(
            form.is_valid(),
            msg="No name was provided, but the form is valid!")
    
    def test_email_is_required(self):
        """Test for the 'email' field"""
        form = ContactForm({
            'name': 'tester',
            'email': '',
            'reason': 'question',
            'message': 'test'
        })
        self.assertFalse(
            form.is_valid(),
            msg="No email was provided, but the form is valid!")
        
    def test_reason_is_required(self):
        """Test for the 'reason' field"""
        form = ContactForm({
            'name': 'tester',
            'email': 'test@test.com',
            'reason': '',
            'message': 'test'
        })
        self.assertFalse(
            form.is_valid(),
            msg="No reason was provided, but the form is valid!")
        
    def test_message_is_required(self):
        """Test for the 'message' field"""
        form = ContactForm({
            'name': 'tester',
            'email': 'test@test.com',
            'reason': 'question',
            'message': ''
        })
        self.assertFalse(
            form.is_valid(),
            msg="No message was provided, but the form is valid!")
