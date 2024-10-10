from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=30, blank=True)
    phone_number = models.IntegerField()
    profile_picture = models.ImageField(upload_to='user_profile/%Y/%m/%d', blank=True)
    cover_image = models.ImageField(upload_to='user_cover/%Y/%m/%d', blank=True)
    
    def __str__(self):
        return self.user.username
