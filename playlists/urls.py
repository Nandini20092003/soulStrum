# playlists/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.playlist_list, name='playlist_list'),
    path('create/', views.create_playlist, name='create_playlist'),
]
