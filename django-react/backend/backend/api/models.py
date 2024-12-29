from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User , on_delete=models.CASCADE , related_name="notes") #each user can have many notes , 
    #related name helps access [user.notes] , on_delete option means that if user is deleted then all the notes of that user are
    # are also deleted 
    
    def __str__(self):
        return self.title
    


