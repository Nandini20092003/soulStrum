# music_catalog/models.py

from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='artist_images', blank=True)

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to='album_covers', blank=True)

    def __str__(self):
        return self.title

class Track(models.Model):
    title = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    duration = models.DurationField()
    audio_file = models.FileField(upload_to='audio_files')


    def __str__(self):
        return self.title

