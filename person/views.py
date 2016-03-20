from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
from bus.models import Bus_schedule
from .models import Passenger, Driver
from .forms import LoginForm, UserForm, UserDetailForm

@login_required(login_url='/login/')
def home(request):
	bus_schedules = Bus_schedule.objects.all()
	context = {
		"bus_schedules": bus_schedules,
	}
	return render(request, "home.html", context)

@login_required(login_url='/login/')
def reservation(request):
	origin = request.POST.get('origin', None) 
	destination = request.POST.get('destination', None)

	results = Bus_schedule.objects.filter(origin=origin, destination=destination)
	context = {
		"results": results,
	}
	return render(request, "reservation.html", context)

@login_required(login_url='/login/')
def drivers(request):
	drivers = Driver.objects.all()
	context = {
		"drivers": drivers,
	}
	return render(request, "drivers.html", context)

def register(request):

	user_form = UserForm(request.POST or None)
	detail_form = UserDetailForm(request.POST or None)

	if user_form.is_valid() and detail_form.is_valid():
		#save into database
		user = user_form.save()
		user.set_password(user.password)
		user.save()

		detail = detail_form.save(commit=False)
		detail.user_id = user
		detail.save()

		return HttpResponseRedirect("/")

	context = {
		"user_form": user_form,
		"detail_form": detail_form,
	}
	return render(request, "register.html", context)


def login_view(request):
	validation = 1
	form = LoginForm(request.POST or None)
		
	if form.is_valid():
		validation = 0

		username = form.cleaned_data['username']
		password = form.cleaned_data['password']

		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect("/")

	context = {
		"form": form,
		"validation": validation,
	}
	return render(request, "login.html", context)

@login_required(login_url='/login/')
def logout_view(request):
	logout(request)
	return HttpResponseRedirect("/")

