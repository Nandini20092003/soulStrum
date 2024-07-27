# music_catalog/views.py

from django.shortcuts import get_object_or_404, render
from .models import Artist, Album, Track
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


#artist
def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'music_catalog/artist_list.html', {'artists': artists})

def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    return render(request, 'music_catalog/artist_detail.html', {'artist': artist})

#album
def album_list(request):
    albums = Album.objects.all()
    return render(request, 'music_catalog/album_list.html', {'albums': albums})

def album_detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music_catalog/album_detail.html', {'album': album})

#track
def track_list(request):
    tracks = Track.objects.all()
    return render(request, 'music_catalog/track_list.html', {'tracks': tracks})

def track_detail(request, track_id):
    track = get_object_or_404(Track, pk=track_id)
    return render(request, 'music_catalog/track_detail.html', {'track': track})

