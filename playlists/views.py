# playlists/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Playlist

@login_required
def playlist_list(request):
    playlists = Playlist.objects.filter(user=request.user)
    return render(request, 'playlists/playlist_list.html', {'playlists': playlists})

@login_required
def create_playlist(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        playlist = Playlist.objects.create(name=name, user=request.user)
        return redirect('playlist_list')
    return render(request, 'playlists/create_playlist.html')
