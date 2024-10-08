# Generated by Django 4.2.14 on 2024-08-01 08:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['-created_on']},
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(max_length=500, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='reason',
            field=models.CharField(choices=[('question', 'Question'), ('feedback', 'Feedback'), ('collaboration', 'Collaboration Request'), ('other', 'Other')], default='question', max_length=30),
        ),
    ]
