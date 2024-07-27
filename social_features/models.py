# social_features/models.py
from django.db import models
from django.contrib.auth.models import User
from music_catalog.models import Track

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'track']

    def __str__(self):
        return f"{self.user.username} likes {self.track.title}"
