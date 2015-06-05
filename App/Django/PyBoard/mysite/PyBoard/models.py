from django.db import models
from django import forms
import django


# Create your models here.

class UserInfo(models.Model):
	""" ユーザ情報 """
	name = models.CharField(max_length=32, unique=True, blank=False,)
	password = models.CharField(max_length=256, blank=False,)
	create_datetime = models.DateTimeField(default=django.utils.timezone.now)
	del_flag = models.IntegerField(default=0)

	def __str__(self):
		return self.name

class Board(models.Model):
	""" 掲示板 """
	topic = models.CharField(max_length=512)
	create_user = models.ForeignKey(UserInfo)
	create_datetime = models.DateTimeField(default=django.utils.timezone.now)
	del_flag = models.IntegerField(default=0)

	def __str__(self):
		return self.topic

class TopicArticle(models.Model):
	""" トピック記事 """
	topic_id = models.ForeignKey(Board)
	article_no = models.IntegerField()
	create_user = models.ForeignKey(UserInfo)
	article = models.TextField(blank=True)
	create_datetime = models.DateTimeField(default=django.utils.timezone.now)
	del_flag = models.IntegerField(default=0)

	def __str__(self):
		return self.article


