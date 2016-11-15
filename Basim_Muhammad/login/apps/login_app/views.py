from django.shortcuts import render,redirect
from django.contrib import messages
from .models import User,UserManager
import bcrypt

def index(request):
	return render(request,'index.html')

def registration(request):
	result=User.objects.validate_registration([request.POST['first_name'],request.POST['last_name'],request.POST['email'],request.POST['password'],request.POST['confirm_password']])
	print result
	user_first=request.POST['first_name']
	user_last=request.POST['last_name']
	user_email=request.POST['email']
	user_password=request.POST['password']
	user_confirm=request.POST['confirm_password']
	if len(result)>0:
		for error in result:
			messages.warning(request, error)
		return redirect ('/')
	else:
		pw_bytes = user_password.encode('utf-8')
		hash_pw=bcrypt.hashpw(pw_bytes,bcrypt.gensalt())
		messages.success(request, 'Registration Complete!')
		insert=User(first_name=user_first,last_name=user_last,email=user_email,hash_pw=hash_pw)
		insert.save()
		return redirect('/')

def login (request):
	result=User.objects.validate_login(request.POST['email'],request.POST['password'])
	for error in result:
		messages.warning(request, error)
	return redirect('/')


# Create your views here.
