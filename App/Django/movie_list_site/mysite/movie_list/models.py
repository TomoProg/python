from django.db import models
from django.utils import timezone
from django.conf import settings
import os
import django

# Create your models here.

class Genre(models.Model):
	name = models.CharField(max_length=200, unique=True)

	def __str__(self):
		return self.name

class Movie(models.Model):
	title = models.CharField(max_length=200)
	genre = models.ForeignKey(Genre, default=1)
	NUM_STARS_CHOICE = (
		(0,0),
		(1,1),
		(2,2),
		(3,3),
		(4,4),
		(5,5),
	)
	num_stars = models.IntegerField(choices=NUM_STARS_CHOICE)
	pic = models.ImageField(upload_to=os.path.join(settings.MEDIA_ROOT, "upload"), default=os.path.join(settings.MEDIA_ROOT, 'default_image.png'))
	#picture_path = models.CharField(max_length=1024, blank=True)
	note = models.TextField(blank=True)
	regist_date = models.DateTimeField('date registered', default=django.utils.timezone.now)
	def __str__(self):
		return self.title

