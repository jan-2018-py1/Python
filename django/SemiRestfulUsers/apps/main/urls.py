from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'users$', views.index, name="home"),
    url(r'users/new$', views.new, name="new"),
    url(r'users/(?P<id>\d+)/edit$', views.edit, name="edit"),
    url(r'users/(?P<id>\d+)$', views.show, name="show"),
    url(r'users/create$', views.create, name="create"),
    url(r'users/(?P<id>\d+)/destroy$', views.destroy, name="delete"),
    url(r'users/update$', views.update, name="update")
]