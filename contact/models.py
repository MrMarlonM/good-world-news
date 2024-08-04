from django.db import models
from django.core.validators import MinLengthValidator

CHOICES = [
    ('question', 'Question'),
    ('feedback', 'Feedback'),
    ('collaboration', 'Collaboration Request'),
    ('other', 'Other')
]


class Contact(models.Model):
    """
    Represents a contact message submitted by a user.
    """
    name = models.CharField(validators=[MinLengthValidator(3)], max_length=200)
    email = models.EmailField()
    reason = models.CharField(max_length=30, choices=CHOICES, default='question')
    message = models.TextField(validators=[MinLengthValidator(10)], max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Orders contact messages by their creation date in descending order (newest first).
        """
        ordering = ["-created_on"]
    
    def __str__(self):
        """
        Returns a string representation of the contact message in the format: "[reason] by [name]".
        """
        return f"{self.reason} by {self.name}"