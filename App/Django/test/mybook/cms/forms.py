#-*- coding:utf-8 -*-
from django.forms import ModelForm
from cms.models import Book

class BookForm(ModelForm):
	''' 書籍フォーム '''
	class Meta:
		model = Book
		fields = ('name', 'publisher', 'page', )
