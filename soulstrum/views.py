# soulstrum/views.py

from django.shortcuts import render
from music_catalog.models import Artist, Album, Track
from playlists.models import Playlist
from recommendations.models import Recommendation

def home(request):
    artists = Artist.objects.all()[:5]  
    albums = Album.objects.all()[:5]  
    tracks = Track.objects.all()[:5]  
    playlists = Playlist.objects.all()[:5]  
    recommendations = Recommendation.objects.all()[:5]  

    return render(request, 'home.html', {
        'artists': artists,
        'albums': albums,
        'tracks': tracks,
        'playlists': playlists,
        'recommendations': recommendations
    })

