# Generated by Django 5.0.1 on 2024-01-21 19:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Main", "0002_classimage_remove_post_images_post_images"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="images",
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="post_images/")),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="Main.post",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="ClassImage",
        ),
    ]
