from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import RequestContext
from PyBoard.forms import LoginForm
from PyBoard.forms import CreateUserForm
from PyBoard.forms import TopicListForm
from PyBoard.forms import CreateAuthForm
from PyBoard.models import UserInfo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def encrypt(src):
	# 暗号化
	if type(src) is not str:
		return False
	encrypt_str = src
	return encrypt_str

def login(request):
	""" ログインページ """
	info_ret = 0
	if request.method == 'POST':
		f = LoginForm(request)
		name = request.POST['name']
		password = request.POST['password']
		try:
			user_info = UserInfo.objects.get(name=name, password=password)
			return redirect('PyBoard:topic_list')
		except:
			f = LoginForm()
			info_ret = -1
	else:
		f = LoginForm()

	return render_to_response('PyBoard/source/html/login.html',
								{'form1':f, 'info_ret':info_ret, },
								context_instance=RequestContext(request))

def create_user(request):
	""" ユーザ作成ページ """
	info_ret = 0
	if request.method == 'POST':
		f = CreateUserForm(request)
		name = request.POST['name']
		password = request.POST['password']
		if len(name) != 0 and len(password) != 0:
			try:
				encrypt_pass = encrypt(password)
				user_info = UserInfo(name=name, password=encrypt_pass)
				user_info.save()
				return redirect('PyBoard:login')
			except:
				f = CreateUserForm()
				info_ret = -1
		else:
			f = CreateUserForm()
			info_ret = -1
	else:
		f = CreateUserForm()

	return render_to_response('PyBoard/source/html/create_user.html',
								{'form1':f, 'info_ret':info_ret},
								context_instance=RequestContext(request))

def topic_list(request, name=None, password=None):
	""" トピックリストページ """
	return render_to_response('PyBoard/source/html/topic_list.html',
							{},
							context_instance=RequestContext(request))

def topic(request, topic_id):
	""" トピックページ """
	html = """
		<html>
		<body>
		<h1>Topic Page</h1>
		<p>topic_id %s</p>
		</body>
		</html>
		""" % (topic_id)
	return HttpResponse(html)

def create_auth(request):
	""" ユーザ作成ページ """
	if request.method == 'POST':
		f = CreateAuthForm(request.POST)
		username = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		print(username)
		print(password1)
		print(password2)
	else:
		f = CreateAuthForm()
	return render_to_response('PyBoard/source/html/create_auth.html',
							{'form':f},
							context_instance=RequestContext(request))
