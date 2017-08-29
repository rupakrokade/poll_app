# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return render(request,'polls/home.html')

def contact(request):
    return render(request, 'polls/basic.html', {'content':['You can contact me at','rupakrokade@gmail.com']})
