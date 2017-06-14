from django.conf.urls import url
from . import nviews,views
app_name = 'music'
urlpatterns = [
	# /music/
    #url(r'^$', views.index, name = 'index'),
    url(r'^$', nviews.IndexView.as_view(), name = 'index'),

    # /register/
    url(r'^register/$', nviews.UserFormView.as_view(), name = 'register'),

    # /music/album_id
    #rl(r'^(?P<album_id>[0-9]+)/$', views.detail, name= "detail"),

    # /music/album_id
    url(r'^(?P<pk>[0-9]+)/$', nviews.DetailView.as_view(), name= "detail"),

    #/music/album_id/favourite  to  /music/album_id
    url(r'^(?P<album_id>[0-9]+)/favourite$', nviews.favourite, name= "favourite"),

    # /music/album/add
    url(r'^album/add$',nviews.AlbumCreate.as_view(), name = 'add_album'),

    # /music/album/album_id/
    url(r'^album/(?P<pk>[0-9]+)/$',nviews.AlbumUpdate.as_view(), name = 'update_album'),

    # /music/album/album_id/delete
    url(r'^album/(?P<pk>[0-9]+)/delete/$',nviews.AlbumDelete.as_view(), name = 'delete_album'),

    # /music/album_id/song/add
    url(r'^song/add/$',nviews.SongCreate.as_view(), name= 'add_song'),

    # /music/album_id/song/song_id/
    url(r'^song/(?P<pk>[0-9]+)/$',nviews.SongUpdate.as_view(), name='update_song'),

    # /music/album_id/song/song_id/delete
    url(r'^song/(?P<pk>[0-9]+)/delete$',nviews.SongDelete.as_view(), name='delete_song'),
]