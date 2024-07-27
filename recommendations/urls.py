# recommendations/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.recommendation_list, name='recommendation_list'),
    path('artists/', views.artist_list, name='artist_list'),
    path('artist/<int:artist_id>/', views.artist_detail, name='artist_detail'),
    path('albums/', views.album_list, name='album_list'),
    path('album/<int:album_id>/', views.album_detail, name='album_detail'),
    path('tracks/', views.track_list, name='track_list'),
    path('track/<int:track_id>/', views.track_detail, name='track_detail'),
]
