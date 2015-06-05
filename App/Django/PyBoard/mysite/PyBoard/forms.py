from django.forms import ModelForm
from PyBoard.models import UserInfo
from PyBoard.models import Board
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(ModelForm):
	class Meta:
		model = UserInfo
		widgets = {'password':forms.PasswordInput(),}
		fields = ('name', 'password', )

class CreateUserForm(ModelForm):
	class Meta:
		model = UserInfo
		fields = ('name', 'password', )

class TopicListForm(ModelForm):
	class Meta:
		model = Board
		fields = ('topic', 'create_datetime', )

class CreateAuthForm(UserCreationForm):
	class Meta:
		model = User
		fields = (	'username',
					'password1',
					'password2',
					)
