from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$',views.index,name='index'),
	url(r'^add$', views.add,name='add'),
	url(r'^delete/(?P<id>\d+)$',views.delete,name='delete'),
	url(r'^delete/confirm/(?P<id>\d+)$',views.confirm,name='confirm'),
	url(r'^management$',views.management,name='management'),
	url(r'^management_update$',views.management_update,name='management_update')
]