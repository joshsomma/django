#from django.http import Http404
#from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Album

def index(request):
    #connect to dbase
    all_albums = Album.objects.all()
    #create html tmpl
    #template = loader.get_template('music/index.html')
    #context = {'all_albums' : all_albums}
    #return HttpResponse(template.render(context,request))
    return render(request,'music/index.html', {'all_albums' : all_albums})

def detail(request, album_id):
    #return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")
    album = get_object_or_404(Album, pk=album_id)
    #try:
        #album = Album.objects.get(pk=album_id)
    #except Album.DoesNotExist:
        #raise Http404("Album does not exist")
    return render(request,'music/detail.html', {'album' : album})
