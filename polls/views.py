# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from polls.forms import UserRegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.views import View

# Create your views here.

from django.http import HttpResponse

#def index(request):
 #   return render(request,'polls/login.html')

def contact(request):
    return render(request, 'polls/basic.html', {'content':['You can contact me at','rupakrokade@gmail.com']})


def register_view(request):
	if request.method=='POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			#u_name, pwd, user_email, key = form.save()
			form.save()
			#return redirect('/login')
			user = authenticate(username=username, password=password)
			login(request, user)

			return redirect('index')
		else:
			return render(request,'polls/register.html', {'form': form})
	else:
		form = UserRegisterForm()
		return render(request,'polls/register.html', {'form':form})

def index(request):
	if request.method=='POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			#u_name, pwd, user_email, key = form.save()
			#return redirect('/login')
			user = authenticate(username=username, password=password)
			login(request, user)

			return redirect('contact')
		else:
			return render(request,'polls/login.html', {'form': form})
	else:
		form =  LoginForm()
		return render(request,'polls/login.html',{'form':form})

def logout(request):
	logout(request)
	return render(request,'polls/logged_out.html')
