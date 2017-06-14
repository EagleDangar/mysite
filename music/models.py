# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models


class Album(models.Model):
	artist = models.CharField(max_length = 250)
	album_title  = models.CharField(max_length = 500)
	genre  = models.CharField(max_length = 100)
	album_logo  = models.FileField()
	#logo_path = models.CharField(max_length = 5000)

	def get_absolute_url(self):
		#return reverse("detail" , kwargs={ "pk" : self.id})
		return '/music/%i/' %self.id

	def __str__(self):
		return self.album_title + ' :- ' + self.artist 
class Song(models.Model):
	album = models.ForeignKey(Album , on_delete=models.CASCADE)
	file_type  = models.CharField(max_length = 10)
	song_title  = models.CharField(max_length = 250)
	is_favourite = models.BooleanField(default=False)
	song_path = models.FileField()

	def get_absolute_url(self):
		return '/music/%i/' %self.album.id

	def __str__(self):
		return self.song_title