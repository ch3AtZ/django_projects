from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Note

from rest_framework import generics
from .serializers import UserSerializer , NoteSerializers 
from rest_framework.permissions import IsAuthenticated  , AllowAny




class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer #connecting all the routes.. 
    permission_classes = [AllowAny]



class NoteListCreate(generics.ListAPIView):
    serializer_class = NoteSerializers
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author= user)
    
    def perform_create(self , serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)


class NoteDelete(generics.DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author= user)