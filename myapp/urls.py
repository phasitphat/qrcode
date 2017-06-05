from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /index/5/
    url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail'),
]