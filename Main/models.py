import os
import uuid

from PIL import Image
from django.core.files.storage import default_storage
from django.db import models


def unique_image_name(instance, filename):
    ext = filename.split(".")[-1]
    name = uuid.uuid4()
    full_name = f"{name}.{ext}"
    return os.path.join("Media/", full_name)


class ClassImage(models.Model):
    image = models.ImageField(upload_to=unique_image_name)


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    images = models.ManyToManyField(ClassImage)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)
        for image in self.images.all():
            with default_storage.open(image.name) as img_file:
                img = Image.open(img_file)
                if img.height > 400 or img.width > 400:
                    output_size = (400, 400)
                    img.thumbnail(output_size)
                    img.save(img_file, format=img.format)
