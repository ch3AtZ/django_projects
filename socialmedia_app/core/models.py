from django.db import models
from django.contrib.auth import get_user_model
import uuid 
from datetime import datetime


User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id_user = models.IntegerField()
    profile_img =models.ImageField(upload_to='profile_images',default='/Users/dhruvbharara/djangoproject/socialmedia_app/media/blank_default_pp.webp')
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100,blank=True)
    name = models.CharField(max_length=20 ,blank=True )

    def __str__(self):
        return self.user.username
    

    
    



class Post(models.Model):
    id = models.UUIDField(primary_key=True , default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    num_likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=datetime.now)

    
    def __str__(self):
        return self.user

