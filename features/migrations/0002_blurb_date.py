# Generated by Django 5.0.4 on 2024-04-11 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blurb',
            name='date',
            field=models.DateTimeField(default=None),
        ),
    ]
