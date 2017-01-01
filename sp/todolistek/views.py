from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

from django.contrib.auth.models import User
from .models import Opravilo

def home (request,user_id):
	context = {}
	return render(request, 'todolistek/home.html', context)

def urediOpraviala (request,user_id):
	context = {}
	return render(request, 'todolistek/urediOpraviala.html', context)
	
def grafAktivnosti (request,user_id):
	context = {}
	return render(request, 'todolistek/grafAktivnosti.html', context)

def nastavitve (request,user_id):
	context = {}
	return render(request, 'todolistek/nastavitve.html', context)	
	
def prijava(request):
	context = {}
	return render(request, 'todolistek/prijava.html', context)

def registracija(request):
	context = {}
	return render(request, 'todolistek/registracija.html', context)	