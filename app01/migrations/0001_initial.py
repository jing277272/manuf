# Generated by Django 3.1.6 on 2021-07-05 15:33

import app01.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('org', models.CharField(blank=True, max_length=128, verbose_name='Organization')),
                ('avatar', models.ImageField(default='avatar/default.jpg', upload_to=app01.models.user_directory_path, verbose_name='头像')),
                ('join_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='join date')),
                ('mod_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Mod date')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
            },
        ),
    ]