# Generated by Django 4.2.14 on 2024-07-28 12:28

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0002_article_is_breaking_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
