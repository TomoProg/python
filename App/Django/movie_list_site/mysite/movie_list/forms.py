#-*- coding:utf-8 -*-
from django.forms import ModelForm
from movie_list.models import Movie

class MovieForm(ModelForm):
	''' 映画フォーム '''
	class Meta:
		model = Movie
		fields = ('title', 'genre', 'num_stars', 'note', )
