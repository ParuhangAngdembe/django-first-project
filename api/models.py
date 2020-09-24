from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

class Category(models.Model):
    title=models.CharField(max_length=30)
    description=models.TextField()

class Tag(models.Model):
    title=models.CharField(max_length=30)
