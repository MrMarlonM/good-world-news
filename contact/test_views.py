from django.test import TestCase
from django.urls import reverse
from .forms import ContactForm


class TestContactView(TestCase):
    
    def test_render_contact_form(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(
            response.context['form'], ContactForm
        )
    
    def test_successful_contact_form_submission(self):
        """Test for someone trying to contact the website owner"""
        contact_data = {
            'name': 'test name',
            'email': 'test@test.com',
            'reason': 'question',
            'message': 'This is my message'
        }
        response = self.client.post(
            reverse('contact'), contact_data, follow=True)
        self.assertRedirects(response, reverse('home'))
        self.assertIn(
            b"Your message was sent successfully.",
            response.content)
