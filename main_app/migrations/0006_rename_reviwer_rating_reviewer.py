# Generated by Django 4.0.4 on 2022-04-23 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_rating_created_at_delete_request'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='reviwer',
            new_name='reviewer',
        ),
    ]
