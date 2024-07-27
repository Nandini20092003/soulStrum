# social_features/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from music_catalog.models import Track
from .models import Like

@login_required
def like_track(request, track_id):
    if request.method == 'POST':
        track = Track.objects.get(pk=track_id)
        like, created = Like.objects.get_or_create(user=request.user, track=track)
        if not created:
            like.delete()
    return redirect('track_detail', track_id=track_id)
