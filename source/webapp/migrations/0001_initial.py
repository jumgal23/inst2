# Generated by Django 5.0.2 on 2024-02-09 03:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='publication/picture/', verbose_name='Аватар')),
                ('description', models.TextField(verbose_name='Описание')),
                ('likes_count', models.PositiveIntegerField(default=0, verbose_name='Счетчик лайков')),
                ('comments_count', models.PositiveIntegerField(default=0, verbose_name='Счетчик комментариев')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publications', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('users_like', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]