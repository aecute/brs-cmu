from django.conf.urls import url
from django.contrib import admin

from .views import (
	home,
	login_view,
	logout_view,
	register,
	reservation,
	drivers,
	)

urlpatterns = [
	url(r'^$', home),
    url(r'^login/$', login_view),
    url(r'^logout/$', logout_view, name="logout"),
    url(r'^register/$', register), 
    url(r'^reservation/$', reservation), 
    url(r'^drivers/$', drivers), 
]
