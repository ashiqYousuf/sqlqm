from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150)
    is_digital = models.BooleanField(default=False)

    def __str__(self):
        return self.name
