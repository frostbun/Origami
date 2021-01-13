from django.contrib import admin
from OrigamiApp.models import UserProfile, UserBlog, Comment

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(UserBlog)
admin.site.register(Comment)