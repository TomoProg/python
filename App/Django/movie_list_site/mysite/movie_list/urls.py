# -*- coding:utf-8 -*-
from django.conf.urls import patterns, url
from movie_list import views

urlpatterns = patterns('',
    url(r'^$', 'movie_list.views.index', name='index'),
    url(r'^add/$', 'movie_list.views.movie_edit', name='movie_add'),
    url(r'^edit/(?P<movie_id>\d+)/$', 'movie_list.views.movie_edit', name='movie_edit'),
    url(r'^del/(?P<movie_id>\d+)/$', 'movie_list.views.movie_del', name='movie_del'),
) 
