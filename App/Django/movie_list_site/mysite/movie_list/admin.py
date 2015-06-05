from django.contrib import admin
from movie_list.models import Genre, Movie

# Register your models here.

class GenreAdmin(admin.ModelAdmin):
	list_display = ('name',)
admin.site.register(Genre, GenreAdmin)

class MovieAdmin(admin.ModelAdmin):
	list_display = ('id', 
					'title',
					'genre',
					'num_stars',
					'pic',
					'note',
					'regist_date',
	)
admin.site.register(Movie, MovieAdmin)

