from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = any)
    pic = models.ImageField(upload_to = 'profile_pics', blank = True, )

    def __str__(self):
        return self.user.username

class UserBlog(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=any)
    blog = models.CharField(max_length = 1000000000)

    def __str__(self):
        return self.user.username + '\'s blog'