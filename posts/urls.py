from django.conf.urls import url
from django.contrib import admin

from .views import (
	post_home,
	post_create,
	post_delete
	)

urlpatterns = [
    url(r'^$', post_home),
    url(r'^create/$', post_create),
    url(r'^delete/$', post_delete),
]
