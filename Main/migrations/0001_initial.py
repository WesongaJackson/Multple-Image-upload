# Generated by Django 5.0.1 on 2024-01-21 12:33

import Main.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('images', models.ImageField(upload_to=Main.models.unique_image_name)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
