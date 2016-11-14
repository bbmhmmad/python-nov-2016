from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$',views.index),
	url(r'^add$', views.add),
	url(r'^delete/(?P<id>\d+)$',views.delete),
	url(r'^delete/confirm/(?P<id>\d+)$',views.confirm)
]