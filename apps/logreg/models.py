# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt


# Create your models here.
class User_validator(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		if len(postData['first_name']) < 1:
			errors['first_name'] = "Please enter a first name"
		if len(postData['last_name']) < 2:
			errors['last_name'] = "Please enter a last name"
		if len(postData['remail']) < 5:
			errors['remail'] = "Email must be at least 5 characters"
		if len(postData['rpass1']) < 8:
			errors['rpass1'] = "Password must be at least 8 characters"
		if postData['rpass1'] != postData['rpass2']:
			errors['rpass2'] = "Passwords must match"
		return errors

	def login_validator(self, postData):
		errors = []
		if postData['email'] < 5:
			errors.append("email not valid")
		if postData['password'] < 8:
			errors.append('password not valid')
		else:
			userData = User.objects.filter(email=postData['email'])
			
			if userData:
				if bcrypt.checkpw(postData['password'].encode(), userData[0].password.encode()):
					return (True, userData)
				else:
					errors.append('password not valid')
			else:
				errors.append("email not valid")
			return (False, errors)
		return (False, errors)

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)
	objects = User_validator()