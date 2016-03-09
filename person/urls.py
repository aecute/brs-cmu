from django.conf.urls import url
from django.contrib import admin

from .views import (
	login,
	register,
	reservation,
	)

urlpatterns = [
    url(r'^$', login),
    url(r'^register/$', register),
    url(r'^reservation/$', reservation),
    
]
