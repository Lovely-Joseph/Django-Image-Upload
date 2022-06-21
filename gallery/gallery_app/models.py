from django.db import models

# Create your models here.
class imageModel(models.Model):
    title=models.CharField(max_length=100)
    img=models.ImageField(max_length=250)