from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
from bus.models import Bus_schedule, Bus
from .models import Passenger, Driver
from .forms import LoginForm, UserForm, UserDetailForm

@login_required(login_url='/login/')
def home(request):
	#bus_schedules = Bus_schedule.objects.all()
	sql = 'SELECT * FROM bus_bus_schedule'
	bus_schedules = Bus_schedule.objects.raw(sql)
	error = len(list(bus_schedules))

	context = {
		"bus_schedules": bus_schedules,
		"error": error,
	}
	return render(request, "home.html", context)

	# sql = "SELECT * FROM person_passenger"
	# passenger = Passenger.objects.raw(sql)
	
	#count = len(list(passenger))

@login_required(login_url='/login/')
def reservation(request):

	results=None
	error = 0

	# Origin and Destination
	sql = "SELECT origin id, destination FROM bus_bus_schedule GROUP BY origin, destination"
	bus_schedules = Bus_schedule.objects.raw(sql)
	bus_schedules_error = len(list(bus_schedules))

	# bus status
	sql = "SELECT * FROM bus_bus"
	bus = Bus.objects.raw(sql)
	bus_error = len(list(bus))

	if request.method == 'POST':
		origin = request.POST.get('origin') 
		destination = request.POST.get('destination')
		results = Bus_schedule.objects.raw("SELECT * FROM bus_bus_schedule WHERE origin=%s AND destination=%s",[origin,destination])
		#print list(results)
		error = len(list(results))
		
	#results = Bus_schedule.objects.filter(origin=origin, destination=destination)
	context = {
		"bus": bus,
		"bus_schedules": bus_schedules,
		"bus_schedules_error": bus_schedules_error,
		"results": results,
		"error": error,
		# "origins_error":origins_error,
		# "destinations_error": destinations_error,
	}
	return render(request, "reservation.html", context)

@login_required(login_url='/login/')
def ticket(request, id=None):

	path = Bus_schedule.objects.raw("SELECT * FROM bus_bus_schedule WHERE id=%s",[id])
	#path = Bus_schedule.objects.filter(id=id) 
	profile = Passenger.objects.raw("SELECT * FROM person_passenger WHERE user_id_id=%s",[request.user.id])
	

	context = {
		"id": id,
		"path": path,
		"profile": profile,
	}
	return render(request, "ticket.html", context)

@login_required(login_url='/login/')
def drivers(request):
	#drivers = Driver.objects.all()
	drivers = Driver.objects.raw("SELECT * FROM person_driver")
	error = len(list(drivers))
	context = {
		"drivers": drivers,
		"error": error,
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

