from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

from django.contrib.auth.models import User
from .models import Opravilo

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.translation import activate

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required

import sys

from .forms import LoginForm

def home (request):
	
	context = {'loginForm':LoginForm()}
  #article_list = Article.objects.order_by('-pub_date')[:5]
  #context['articles'] = article_list
  
  if request.method=='POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
      if user is not None:
        login(request, user)
     
  else:
    form = LoginForm()
  context['loginForm'] = form
  return render(request, 'todolistek/home.html', context)


def urediOpraviala (request):
	context = {}
	return render(request, 'todolistek/urediOpraviala.html', context)
	
def grafAktivnosti (request):
	context = {}
	return render(request, 'todolistek/grafAktivnosti.html', context)

def nastavitve (request):
	context = {}
	return render(request, 'todolistek/nastavitve.html', context)	
	
def prijava(request):
	context = {}
	return render(request, 'todolistek/prijava.html', context)

def registracija(request):
	context = {}
	return render(request, 'todolistek/registracija.html', context)	
	
def odjava(request):
  logout(request)
  return HttpResponseRedirect(reverse('todolistek.html'))