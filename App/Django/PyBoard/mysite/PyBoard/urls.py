#-*- coding:utf-8 -*-
from django.conf.urls import patterns, url
from PyBoard import views

urlpatterns = patterns('',
	url(r'^login/$', views.login, name='login'),
	url(r'^create_user/$', views.create_user, name='create_user'),
	url(r'^create_auth/$', views.create_auth, name='create_auth'),
	url(r'^topic_list/$', views.topic_list, name='topic_list'),
	url(r'^topic_list/(?P<topic_id>\d+)/$', views.topic, name='topic'),
)
