from django.db import models
from django.core.validators import MinLengthValidator

CHOICES = [
    ('question', 'Question'),
    ('feedback', 'Feedback'),
    ('collaboration', 'Collaboration Request'),
    ('other', 'Other')
]

# Create your models here.
class Contact(models.Model):
    name = models.CharField(validators=[MinLengthValidator(3)], max_length=200)
    email = models.EmailField()
    reason = models.CharField(max_length=30, choices=CHOICES, default='question')
    message = models.TextField(validators=[MinLengthValidator(10)], max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]
    
    def __str__(self):
        return f"{self.reason} by {self.name}"