from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader, RequestContext
from movie_list.models import Movie
from movie_list.forms import MovieForm

# Create your views here.

def index(request):
	movies = Movie.objects.all().order_by('id')
	return render_to_response('movie_list/movie_list.html',
								{'movies': movies},
								context_instance=RequestContext(request))

def movie_edit(request, movie_id=None):
	if movie_id:
		movie = get_object_or_404(Movie, pk=movie_id)
	else:
		movie = Movie()
	
	if request.method == 'POST':
		form = MovieForm(request.POST, instance=movie)
		if form.is_valid():
			movie = form.save(commit=False)
			movie.save()
			return redirect('movie_list:index')
	else:
		form = MovieForm(instance=movie)

	return render_to_response('movie_list/movie_edit.html',
								dict(form=form, movie_id=movie_id),
								context_instance=RequestContext(request))

def movie_del(request, movie_id):
	movie = get_object_or_404(Movie, pk=movie_id)
	movie.delete()
	return redirect('movie_list:index')

#def movie_detail(request, movie_id):
#	movie = get_object_or_404(Movie, pk=movie_id)
#	return render_to_response('movie_list/movie_edit.html',
#								dict(form=form, movie_id=movie_id),
#								context_instance=RequestContext(request))


