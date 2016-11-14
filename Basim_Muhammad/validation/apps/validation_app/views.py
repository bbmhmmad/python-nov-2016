from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Email

def index(request):
	return render (request,'index.html')

def process(request):
	if Email.objects.validate(request.POST['email'])==False:
		messages.warning(request, 'Invalid email')
		return redirect ('/')
	else:
		messages.success(request, 'Email Successfully Stored!')
		Email.objects.create(email=request.POST['email'])
		context={'data':Email.objects.all()}
		return render (request,'results.html',context)

# Create your views here.
