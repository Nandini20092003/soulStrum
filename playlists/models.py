# playlists/models.py
from django.db import models
from django.contrib.auth.models import User
from music_catalog.models import Track

class Playlist(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tracks = models.ManyToManyField(Track)

    def __str__(self):
        return self.name
