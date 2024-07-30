from django.db import models

CHOICES = [
    ('question', 'Question'),
    ('feedback', 'Feedback'),
    ('collaboration', 'Collaboration Request'),
    ('other', 'Other')
]

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    reason = models.CharField(max_length=30, choices=CHOICES)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)