from django.shortcuts import render, get_object_or_404
from .models import Album, Song

def index(request):
    allAlbums = Album.objects.all()
    return render(request, 'music/index.html', {'allAlbums' : allAlbums})

def detail(request, albumId):
    album = get_object_or_404(Album, pk = albumId)
    return render(request, 'music/detail.html', {'album' : album})

def favorite(request, albumId):
    album = get_object_or_404(Album, pk = albumId)
    try:
        selectSong = album.song_set.get(pk = request.POST['song'])
    except(KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album' : album,
        })