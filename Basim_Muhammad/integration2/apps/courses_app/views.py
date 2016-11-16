from django.shortcuts import render,redirect
from django.db.models import Count
from django.core.urlresolvers import reverse
from .models import Course
from ..login_app.models import User

def index(request):
	context={
		'data':Course.objects.all()
	}
	return render(request,'courses_app/index.html',context)

def add(request):
	c=Course(name=request.POST['name'],description=request.POST['description'])
	c.save()
	print c
	return redirect (reverse('courses:index'))

def delete(request,id):
	context={
		'data':Course.objects.get(id=id)
	}
	return render (request, 'courses_app/delete.html',context)

def confirm(request,id):
	if request.POST['button']=='NO':
		return redirect (reverse('courses:index'))
	else:
		unwanted=Course.objects.get(id=id)
		unwanted.delete()
		return redirect (reverse('courses:index'))

def management(request):
	totals=Course.objects.all().annotate(count=Count('usertocourse')).values('name','count')
	print totals
	# print Course.objects.all()
	context={'courses':Course.objects.all(),'users':User.objects.all(),'count':totals}	
	return render(request,'courses_app/management.html',context)

def management_update(request):
	# context={'data':Course.objects.all()}	
	user_course=User.objects.get(id=request.POST['user'])
	user_course.course=Course.objects.get(id=request.POST['course'])
	user_course.save()
	print user_course
	return redirect(reverse('courses:management'))


# Create your views here.
