from django.conf.urls import url
from django.contrib import admin

from .views import (
	home,
	login_view,
	logout_view,
	register,
	ticket,
	drivers,
	companys,
	)

urlpatterns = [
	url(r'^$', home),
    url(r'^login/$', login_view),
    url(r'^logout/$', logout_view, name="logout"),
    url(r'^register/$', register), 
    url(r'^ticket/(?P<id>\w+)/$', ticket, name="ticket"),
    url(r'^drivers/$', drivers), 
    url(r'^companys/$', companys), 
]
