from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    pic = models.ImageField(upload_to = 'profile_pics/', blank = True)

    def __str__(self):
        return self.user.username

class UserBlog(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    blog = models.TextField(max_length = 1000000000)
    date_posted = models.DateTimeField(auto_now= True)
    cover = models.ImageField(upload_to = 'blog_covers/', blank = True)

    def __str__(self):
        return self.user.username + '\'s blog'

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
