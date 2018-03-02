# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..logreg.models import User

# Create your models here.
class Quote(models.Model):
	quote = models.CharField(max_length=255)
	user = models.ForeignKey(User, related_name='user_quote')
	usersliking = models.IntegerField() #incriment up or down
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Like(models.Model):
	user = models.ForeignKey(User, related_name='liked_quote')
	quote = models.ForeignKey(Quote, related_name='user_liked')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)