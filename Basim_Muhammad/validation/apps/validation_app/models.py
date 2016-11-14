from __future__ import unicode_literals
from django.db import models
import re
  #Our new manager!
  #No methods in our new manager should ever catch the whole request object with a parameter!!! (just parts, like request.POST)
class UserManager(models.Manager):
  def validate(self, user_email):
	EMAIL_REGEX=r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'
	if not re.match(EMAIL_REGEX,user_email):
		return False 
	else: 
		return True
class Email(models.Model):
  email = models.EmailField(max_length=45)
  created_at = models.DateTimeField(auto_now_add = True)    
  objects = UserManager()

# Create your models here.
