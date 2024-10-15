from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=300)
    hint = models.TextField()

    def __str__(self):
        return self.title
