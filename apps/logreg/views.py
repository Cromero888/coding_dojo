# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import *
import bcrypt
from django.contrib import messages

# Create your views here.
def index(request):
	return render(request, 'login.html')

def register(request):
	errors = User.objects.basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect('/')

	if len(errors) == 0:
		user = User.objects.create()
		hash1 = bcrypt.hashpw(request.POST['rpass1'].encode(), bcrypt.gensalt())
		user.first_name = request.POST['first_name']
		user.last_name = request.POST['last_name']
		user.email = request.POST['remail']
		user.password = hash1
		user.save()
		return redirect('/')

def login(request):
	errors = User.objects.login_validator(request.POST)
	if errors[0] == False:
		for errors in errors[1]:
			messages.error(request, errors)
		return redirect('/')
	if errors[0] == True:
		request.session['user_id'] = errors[1][0].id
		return redirect('/bright_ideas/')

def logout(request):
	request.session.flush()
	return redirect('/')

# def success(request, id):
