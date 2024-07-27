# social_features/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('like/<int:track_id>/', views.like_track, name='like_track'),
]
