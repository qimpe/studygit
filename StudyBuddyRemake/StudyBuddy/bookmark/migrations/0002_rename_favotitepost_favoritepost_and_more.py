# Generated by Django 5.0.3 on 2024-03-19 18:25

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0001_initial'),
        ('postsapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FavotitePost',
            new_name='FavoritePost',
        ),
        migrations.AlterUniqueTogether(
            name='favoritepost',
            unique_together={('user', 'post')},
        ),
    ]