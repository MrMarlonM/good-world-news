from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    A Django ModelForm for creating and editing contact messages.

    Fields:
    - name: The name of the person submitting the message
            (single-line text input).
    - email: The email address of the person submitting the message
             (email input with validation).
    - reason: The reason for the contact, selected from a dropdown menu
              (choices defined in the Contact model).
    - message: The main content of the contact message (textarea).
    """
    class Meta:
        model = Contact
        fields = ['name', 'email', 'reason', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'reason': forms.Select(attrs={'class': 'form-select'}),
            'message': forms.Textarea(attrs={'class': 'form-control'})
        }
