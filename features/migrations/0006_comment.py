# Generated by Django 5.0.4 on 2024-05-04 20:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0005_podcast'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, default='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('blurb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='features.blurb')),
                ('downvotes', models.ManyToManyField(blank=True, related_name='downvotes_comment', to=settings.AUTH_USER_MODEL)),
                ('upvotes', models.ManyToManyField(blank=True, related_name='upvotes_comment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
