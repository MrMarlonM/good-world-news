from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    """
    A Django ModelForm for creating and editing comments.
    """
    class Meta:
        model = Comment
        fields = ['content',]
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'id': 'id_body'})
        }