from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='generated/')
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
