from django.shortcuts import render, get_object_or_404
from .models import Album, Song

def index(request):
    #connect to dbase
    all_albums = Album.objects.all()
    #use render to get list of all albums
    return render(request,'music/index.html', {'all_albums' : all_albums})

def detail(request, album_id):
    #check and see if an album w id is available or return 404 msg
    album = get_object_or_404(Album, pk=album_id)
    #use render to get album details
    return render(request,'music/detail.html', {'album' : album})

def favourite (request,album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request,'music/detail.html', {
        'album':album,
        'error_message': "You did not select a valid song"
        })
    else:
        selected_song.is_favourite = True
        selected_song.save()
        return render(request,'music/detail.html', {'album' : album})
