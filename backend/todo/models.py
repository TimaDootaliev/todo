from django.db import models
from slugify import slugify
from datetime import datetime

class ToDo(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True, primary_key=True)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) + '-' + datetime.now().strftime('%Y%m%d%H%M%S')
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title

    