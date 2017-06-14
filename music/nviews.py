from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from models import Album,Song
from django.contrib.auth import authenticate,login
from django.views.generic import View
from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.shortcuts import render,get_object_or_404
from .forms import UserForm
from django.core.urlresolvers import reverse_lazy

class IndexView(generic.ListView):
    context_object_name = 'all_albums'
    template_name = 'music/index.html'
    model = Album

class DetailView(generic.DetailView):
    template_name = 'music/Details.html'
    model = Album

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
		if selected_song.is_favourite:
			selected_song.is_favourite= False
		else:
			selected_song.is_favourite = True
		selected_song.save()
		return render(request, 'music/Details.html', {'album': album})

class AlbumCreate(CreateView):
	model = Album
	fields = ['artist','album_title', 'genre' , 'album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

class SongCreate(CreateView):
	model = Song
	fields = ['album' , 'file_type' , 'song_title' , 'is_favourite' , 'song_path']

class SongUpdate(UpdateView):
	model = Song
	fields = ['album' , 'file_type', 'song_title' , 'is_favourite' ,'song_path']

class SongDelete(DeleteView):
	model = Song
	print model
	success_url = reverse_lazy('music:index')

class UserFormView(View):
	form_class = UserForm
	template_name = 'music/registration_form.html'

	def get(self,request):
		form = self.form_class(None)
		return render(request,self.template_name, { 'form' : form})

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False)

			#cleaned (normalized) data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			user = authenticate(username= username ,password = password)

			if user is not None:
				if user.is_active:
					login(request,user)
					return redirect('music:index')
		return render(request, self.template_name, {'form': form})