from __future__ import unicode_literals
import re
import bcrypt

from django.db import models
class UserManager(models.Manager):
	def validate_registration(self,user):
		EMAIL_REGEX=r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'
		NAME_REGEX=r'^[A-Za-z0-9_-]*$'
		# result = User.objects.validate_registration(request.POST)
		print user
		errors=[]
		if len(user[0])<2 or len(user[1])<2:
			errors.append('First and last name must be at least 2 characters')
		if User.objects.filter(email=user[2]):
			errors.append('This email is taken.')
		if not re.match(NAME_REGEX,user[0]):
			errors.append('Name can only be letters')
		if not re.match(NAME_REGEX,user[1]):
			errors.append('Name can only be letters')
		if user[2]==0:
			errors.append('Password is required')
		if not re.match(EMAIL_REGEX,user[2]):
			errors.append('Improper email format')
		if user[3]<8:
			errors.append('Password must be greater than 8 characters')
		if user[3]!=user[4]:
			errors.append('Your passwords do not match.')
		return errors
	def validate_login(self,email,password):
		users=User.objects.filter(email=email)
		print users
		pw_bytes = password.encode('utf-8')
		errors=[]
		if len(users)<1:
			print 'if'
			errors.append('No user found. Incorrect email')
		elif users[0].hash_pw!=bcrypt.hashpw(pw_bytes,users[0].hash_pw.encode('utf-8')):
			print 'elif'
			errors.append('No Password match')
		else:
			print 'else'
			errors.append('Successful Login')
		print errors
		return errors


class User(models.Model):
	first_name=models.CharField(max_length=45)
	last_name=models.CharField(max_length=45)
	email=models.EmailField()
	hash_pw=models.CharField(max_length=250)
	created_at=models.DateField(auto_now_add=True)
	updated_at=models.DateField(auto_now=True)

	objects=UserManager()