from django.shortcuts import render,redirect

from .models import Course

def index(request):
	context={
		'data':Course.objects.all()
	}
	return render(request,'index.html',context)

def add(request):
	c=Course(name=request.POST['name'],description=request.POST['description'])
	c.save()
	print c
	return redirect ('/')

def delete(request,id):
	context={
		'data':Course.objects.get(id=id)
	}
	return render (request, 'delete.html',context)

def confirm(request,id):
	if request.POST['button']=='NO':
		return redirect('/')
	else:
		unwanted=Course.objects.get(id=id)
		unwanted.delete()
		return redirect('/')


# Create your views here.
