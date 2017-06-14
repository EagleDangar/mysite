#from django.http import HttpResponse
#from django.http import Http404
from .models import Album,Song
from django.views import generic
from django.shortcuts import render,get_object_or_404
from django.views.generic.edit import CreateView,UpdateView,DeleteView
#from django.template import loader

def index(request):
	all_albums = Album.objects.all()
	#template = loader.get_template('music/index.html')
	context = {
		'all_albums':all_albums,
	}
	#return HttpResponse(template.render(context,request))
	return render(request,'music/index.html',context)

def detail(request, album_id):
	album = get_object_or_404(Album,pk =album_id)
	#return HttpResponse(template.render(context, request))
	return render(request, 'music/Details.html', {'album' : album })
	#return HttpResponse("<title>Details</title><h1>Details for album_id :"+str(album_id)+"</h1>")

def favourite(request, album_id):
	album = get_object_or_404(Album,pk =album_id)
	try:
		selected_song = album.song_set.get(pk = request.POST['song'])
	except (KeyError, Song.DoesNotExist):
		return render(request, 'music/Details.html',
				  {'album' : album ,
				'error_message' : "you did not select a valid song or there is no song in this album"}
					  )
	else:
		selected_song.is_favourite = True
		selected_song.save()
		return render(request, 'music/Details.html', {'album': album})

class AlbumCreate(CreateView):
	model = Album
	fields = ['artist','album_title', 'genre' , 'album_logo' ,'logo_path']