# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from .models import *

# Create your views here.
def index(request):
	context={
		'quote': Quote.objects.all().select_related(),
		'currentuser': User.objects.get(id=request.session['user_id']),
	}
	return render(request, 'table.html', context)

def idea(request):
	idea = Quote.objects.create(
		quote = request.POST['idea'],
		user = User.objects.get(id=request.session['user_id']),
		usersliking = 0,
		)
	idea.save()
	return redirect('/bright_ideas/')

def likeme(request, id):
	print "please halp?"
	update = Quote.objects.get(id=id)
	unlike = Like.objects.filter(quote_id=id, user=request.session['user_id'])
	print unlike
	if len(unlike) > 0:
		update.usersliking -= 1
		update.save()
		unlike.delete()
		return redirect('/bright_ideas/')
	else:
		like = Like.objects.create(
		user= User.objects.get(id=request.session['user_id']),
		quote= Quote.objects.get(id=id)
		)
		update.usersliking += 1
		update.save()
		like.save()
		return redirect('/bright_ideas/')

def user(request, id):
	context={
		'user': User.objects.get(id=id),
		'quote': len(Quote.objects.filter(user_id=id)),
		'likes': len(Like.objects.filter(user_id=id)),
	}
	return render(request, 'user.html', context)

def post(request, id):
	context={
		'quote': Quote.objects.get(id=id),
		'likes': Like.objects.filter(quote=id).select_related(),
	}
	return render(request, 'post.html', context)

def delete(request, id):
	if Quote.objects.get(id=id, user=request.session['user_id']):
		obj = Quote.objects.get(id=id)
		obj.delete()
		return redirect('/bright_ideas/')
	else:
		return redirect('/bright_ideas/')