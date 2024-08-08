from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MinLengthValidator
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Article(models.Model):
    """
    Represents a news article with title, content, author,
    publication status, and other metadata.

    Relationships:
    - `author`: The author of the article (ForeignKey to User).
    - `likes`: Users who have liked the article (ManyToManyField to User
               through the Like model).
    - `comments`: Comments associated with the article (reverse relationship
                  from the Comment model).
    """
    title = models.CharField(
        validators=[MinLengthValidator(1)], max_length=200, unique=True)
    slug = models.SlugField(
        validators=[MinLengthValidator(1)], max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_breaking_news = models.BooleanField(default=False)
    image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(
        validators=[MinLengthValidator(5)], max_length=500, blank=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='article_like', blank=True)

    class Meta:
        """
        Orders articles by their creation date in descending order.
        """
        ordering = ["-created_on"]

    def __str__(self):
        """
        Returns a string representation of the article in the format
        "Title by Author".
        """
        return f"{self.title} by {self.author}"

    def number_of_likes(self):
        """
        Calculates and returns the number of likes for this article.
        """
        return Like.objects.filter(
            content_type=ContentType.objects.get_for_model(Article),
            object_id=self.id).count()


class Comment(models.Model):
    """
    Represents a comment on an article.

    Relationships:
    - `article`: The article this comment is associated with
                 (ForeignKey to Article).
    - `author`: The user who created the comment (ForeignKey to User).
    """
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(
        validators=[MinLengthValidator(1)], max_length=500)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Orders comments by their creation date in descending order.
        """
        ordering = ["-created_on"]

    def __str__(self):
        """
        Returns a string representation of the comment in the format:
        "Comment on - [article title] - by - [author username] -".
        """
        return f"Comment on - {self.article.title} - by - {self.author} -"


class Like(models.Model):
    """
    Represents a "like" action by a user on an article or comment.

    Relationships:
    - `user`: The user who liked the content (ForeignKey to User).
    - `content_type`: The type of content that was liked
                      (ForeignKey to ContentType).
    - `content_object`: The actual object that was liked
                        (either an Article or a Comment would be possible),
                        determined dynamically using
                        `content_type` and `object_id`.
    """
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        """
        Returns a string representation of the like in the format:
        "Like by [user username] on [liked object __str__]".
        """
        return f"Like by {self.user} on {self.content_object}"
