# Generated by Django 5.0.4 on 2024-05-06 22:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0007_alter_comment_downvotes_alter_comment_upvotes'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='blurb',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blurb', to='features.blurb'),
        ),
    ]
