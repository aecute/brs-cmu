from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Passenger, Driver, Bus_schedule, Bus
from .forms import LoginForm, UserForm, UserDetailForm

# connect database
from django.db import connection

from collections import namedtuple

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

@login_required(login_url='/login/')
def home(request):
	#bus_schedules = Bus_schedule.objects.all()
	sql = "SELECT s.bus_schedule_id ,pr.name ori_pr, pl.name ori_pl, date_time_arrive ,pr2.name des_pr, pl2.name des_pl, date_time_depart, bus_id, bc.name company, price FROM brs_cmu_bus_schedule s JOIN brs_cmu_platform pl ON pl.platform_id = s.platform_id_origin_id JOIN brs_cmu_province pr ON pr.province_id = pl.province_id_id JOIN brs_cmu_platform pl2 ON pl2.platform_id = s.platform_id_destination_id JOIN brs_cmu_province pr2 ON pr2.province_id = pl2.province_id_id JOIN brs_cmu_bus b ON b.bus_id=s.bus_id_id JOIN brs_cmu_bus_company bc ON bc.name=b.company_name_id"
	cursor = connection.cursor()
	cursor.execute(sql)
	bus_schedules = namedtuplefetchall(cursor)
	bus_schedules_check = len(bus_schedules)

	context = {
		"bus_schedules": bus_schedules,
		"bus_schedules_check": bus_schedules_check,
	}
	return render(request, "home.html", context)

	# sql = "SELECT * FROM person_passenger"
	# passenger = Passenger.objects.raw(sql)
	
	#count = len(list(passenger))

@login_required(login_url='/login/')
def reservation(request):

	bus_schedules=None
	bus_schedules_check = 0
	bus=None

	cursor = connection.cursor()
	# Origin
	sql = "select pr.name from brs_cmu_bus_schedule bs, brs_cmu_platform pl, brs_cmu_province pr where bs.platform_id_origin_id=pl.platform_id AND pl.province_id_id=pr.province_id group by pr.name order by pr.name"
	cursor.execute(sql)
	origins = namedtuplefetchall(cursor)
	origins_check = len(origins)


	# Destination
	sql = "select pr.name from brs_cmu_bus_schedule bs, brs_cmu_platform pl, brs_cmu_province pr where bs.platform_id_destination_id=pl.platform_id AND pl.province_id_id=pr.province_id group by pr.name order by pr.name"
	cursor.execute(sql)
	destinations = namedtuplefetchall(cursor)
	destinations_check = len(destinations)

	# # bus status
	# sql = "SELECT * FROM bus_bus"
	# bus = Bus.objects.raw(sql)
	# bus_error = len(list(bus))

	if request.method == 'POST':
		origin = request.POST.get('origin') 
		destination = request.POST.get('destination')
		sql = "SELECT s.bus_schedule_id ,pr.name ori_pr, pl.name ori_pl, date_time_arrive ,pr2.name des_pr, pl2.name des_pl, date_time_depart, bus_id, bc.name company, price FROM brs_cmu_bus_schedule s JOIN brs_cmu_platform pl ON pl.platform_id = s.platform_id_origin_id JOIN brs_cmu_province pr ON pr.province_id = pl.province_id_id JOIN brs_cmu_platform pl2 ON pl2.platform_id = s.platform_id_destination_id JOIN brs_cmu_province pr2 ON pr2.province_id = pl2.province_id_id JOIN brs_cmu_bus b ON b.bus_id=s.bus_id_id JOIN brs_cmu_bus_company bc ON bc.name=b.company_name_id where pr.name='%s' and pr2.name='%s'" %(origin,destination)
		cursor.execute(sql)
		bus_schedules = namedtuplefetchall(cursor)
		bus_schedules_check = len(bus_schedules)

		#seat
		# sql = "select b.seats from brs_cmu_bus b where bus_id=(select bs.bus_id_id from brs_cmu_bus_schedule bs where bs.platform_id_origin_id=(select pl.platform_id from brs_cmu_platform pl, brs_cmu_province pr where pl.province_id_id=pr.province_id AND pr.name='%s') AND bs.platform_id_destination_id=(select pl.platform_id from brs_cmu_platform pl, brs_cmu_province pr where pl.province_id_id=pr.province_id AND pr.name='%s'))"%(origin,destination)

		# cursor.execute(sql)
		# bus = namedtuplefetchall(cursor)
		
	context = {
		"origins":origins,
		"origins_check":origins_check,
		"destinations":destinations,
		"destinations_check":destinations_check,
		"bus_schedules":bus_schedules,
		"bus_schedules_check":bus_schedules_check,
		#"bus":bus,
	}
	return render(request, "reservation.html", context)

@login_required(login_url='/login/')
def ticket(request, id=None):

	#path = Bus_schedule.objects.raw("SELECT * FROM bus_bus_schedule WHERE id=%s",[id])
	#path = Bus_schedule.objects.filter(id=id) 
	#profile = Passenger.objects.raw("SELECT * FROM person_passenger WHERE user_id_id=%s",[request.user.id])
	

	context = {
		"id": id,
		# "path": path,
		# "profile": profile,
	}
	return render(request, "ticket.html", context)

@login_required(login_url='/login/')
def drivers(request):
	#drivers = Driver.objects.all()
	error = 0
	context = {
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

