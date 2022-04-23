# Generated by Django 4.0.4 on 2022-04-23 21:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0006_rename_reviwer_rating_reviewer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='reviewee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_reviewee', to=settings.AUTH_USER_MODEL),
        ),
    ]
