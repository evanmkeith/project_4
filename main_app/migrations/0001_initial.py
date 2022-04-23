# Generated by Django 4.0.4 on 2022-04-23 23:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=250)),
                ('rating', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('reviewee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_reviewee', to=settings.AUTH_USER_MODEL)),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image_link', models.CharField(blank=True, max_length=250)),
                ('phone_number', models.CharField(max_length=11)),
                ('zip_code', models.CharField(max_length=5)),
                ('vehicle_type', models.CharField(blank=True, choices=[('Sedan', 'Sedan'), ('Coupe', 'Coupe'), ('Sports Car', 'Sports Car'), ('Station Wagon', 'Station Wagon'), ('Hatchback', 'Hatchback'), ('Convertible', 'Convertible'), ('SUV', 'SUV'), ('Minivan', 'Minivan'), ('Truck', 'Truck')], max_length=15)),
                ('vehicle_make', models.CharField(blank=True, max_length=15)),
                ('vehicle_model', models.CharField(blank=True, max_length=15)),
                ('num_seats', models.IntegerField(blank=True, null=True)),
                ('fee', models.CharField(blank=True, max_length=160)),
                ('bio', models.CharField(blank=True, max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('contacts', models.ManyToManyField(blank=True, related_name='profile_contacts', to=settings.AUTH_USER_MODEL)),
                ('ratings', models.ManyToManyField(blank=True, to='main_app.rating')),
                ('ratings_ive_written', models.ManyToManyField(blank=True, related_name='profile_ratings_ive_written', to='main_app.rating')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
