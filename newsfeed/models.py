from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MinLengthValidator
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Article(models.Model):
    title = models.CharField(validators=[MinLengthValidator(1)], max_length=200, unique=True)
    slug = models.SlugField(validators=[MinLengthValidator(1)], max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_breaking_news = models.BooleanField(default=False)
    image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(validators=[MinLengthValidator(5)], max_length=500, blank=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='article_like', blank=True)

    class Meta:
        ordering = ["-created_on"]
    
    def __str__(self):
        return f"{self.title} by {self.author}"

    def number_of_likes(self):
        return Like.objects.filter(
            content_type=ContentType.objects.get_for_model(Article),
            object_id=self.id).count()


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(validators=[MinLengthValidator(1)], max_length=500)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]
    
    def __str__(self):
        return f"Comment on - {self.article.title} - by - {self.author} -"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"Like by {self.user} on {self.content_object}"