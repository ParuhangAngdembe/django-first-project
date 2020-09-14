from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='static.jpg', upload_to='profile_pics')

    def __str__(self): #dundr
        return f'{self.user.username} Profile'
