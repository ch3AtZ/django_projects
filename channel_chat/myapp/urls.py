from django.contrib import admin
from django.urls import path
from .views import Index , RoomView


urlpatterns = [
    
    path('chat' ,Index.as_view() , name='index' ),
    path('chat/<str:room_name>', RoomView.as_view() , name='room')

    
]