# Generated by Django 4.0.3 on 2022-03-19 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_article_img_alter_article_author_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_img',
        ),
    ]
