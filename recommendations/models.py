# recommendations/models.py
from django.db import models
from music_catalog.models import Track, Album, Artist

class Recommendation(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    reason = models.TextField()


    def __str__(self):
        return f"Recommendation for {self.track.title}"
