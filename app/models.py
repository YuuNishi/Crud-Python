from django.db import models


# Create your models here.
class Profile(models.Model):
    PixivId = models.CharField(max_length=10)
    Email = models.CharField(max_length=30)
    Nick = models.CharField(max_length=30)


