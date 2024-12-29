from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id" , "username" , "password"]
        extra_kwargs = {"passwords":{"write_only":True}} #password cannot be read 

    def create(self , validated_data):
        user = User.objects.create_user(**validated_data) #passing as such as a dictionary .. 
        return user
    
    
class NoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id" , "title" , "content" , "created_at" , "author"]
        extra_kwargs = {"author":{"read_only":True}}  #we should be able to read who the author is but not write who author is 
         