from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$',views.index),
	url(r'^login$', views.login),
	url(r'^registration$', views.registration)
	# url(r'^delete/(?P<id>\d+)$',views.delete),
	# url(r'^delete/confirm/(?P<id>\d+)$',views.confirm)
]