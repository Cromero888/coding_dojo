from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'like/(?P<id>\d+)/', views.likeme),
	url(r'user/(?P<id>\d+)/', views.user),
	url(r'post/(?P<id>\d+)/', views.post),
	url(r'delete/(?P<id>\d+)/', views.delete),
	url(r'idea/', views.idea),
	url(r'^$', views.index),
]