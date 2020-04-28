from django.urls import path, include
from .views import find_room_view,upload_room_view,about_us_view,available_rooms_view

urlpatterns = [
    path('', find_room_view),
    path('find_room/', find_room_view),
    path('upload_room/', upload_room_view),
    path('about_us/', about_us_view),
    path('available_rooms/', available_rooms_view),
]
