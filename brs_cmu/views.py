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

	bus_schedules=None
	bus_schedules_check = 0
	bus=None
	destinations=None
	destinations_check=0

	origin=None
	destination=None

	
	# Origin
	sql = "select pr.name from brs_cmu_bus_schedule bs, brs_cmu_platform pl, brs_cmu_province pr where bs.platform_id_origin_id=pl.platform_id AND pl.province_id_id=pr.province_id group by pr.name order by pr.name"
	cursor = connection.cursor()
	cursor.execute(sql)
	origins = namedtuplefetchall(cursor)
	origins_check = len(origins)
	cursor.close()


	# Destination
	if 'get_des' in request.POST:
		origin = request.POST.get('origin')
		request.session['origin'] = origin
		#print origin

		sql = "select pr.name from brs_cmu_bus_schedule bs, brs_cmu_platform pl, brs_cmu_platform pl2, brs_cmu_province pr, brs_cmu_province pr2 where bs.platform_id_destination_id=pl.platform_id AND pl.province_id_id=pr.province_id and bs.platform_id_origin_id=pl2.platform_id AND pl2.province_id_id=pr2.province_id AND pr2.name='%s' group by pr.name order by pr.name" %(origin)
		cursor = connection.cursor()
		cursor.execute(sql)
		destinations = namedtuplefetchall(cursor)
		destinations_check = len(destinations)
		cursor.close()

	# # bus status
	# sql = "SELECT * FROM bus_bus"
	# bus = Bus.objects.raw(sql)
	# bus_error = len(list(bus))

	if 'search' in request.POST:
		origin = request.session['origin']
		destination = request.POST.get('destination')

		sql = "SELECT bus_schedule_id,pl.name ori_pl,pr.name ori_pr,date_time_arrive, pl2.name des_pl, pr2.name des_pr,date_time_depart, bus_id, bc.name Company,price,seats,COUNT(id_card_id) Booking FROM brs_cmu_bus_schedule s JOIN brs_cmu_platform pl ON pl.platform_id = s.platform_id_origin_id  JOIN brs_cmu_province pr ON pr.province_id = pl.province_id_id JOIN brs_cmu_platform pl2 ON pl2.platform_id = s.platform_id_destination_id JOIN brs_cmu_province pr2 ON pr2.province_id = pl2.province_id_id JOIN brs_cmu_bus b ON b.bus_id = s.bus_id_id JOIN brs_cmu_bus_company bc ON bc.name = b.company_name_id LEFT JOIN brs_cmu_booking bo ON s.bus_schedule_id = bo.bus_schedule_id_id where pr.name='%s' and pr2.name='%s' GROUP BY bus_schedule_id,date_time_arrive ,pl.name,pr.name,date_time_depart, pl2.name , pr2.name, bus_id, bc.name,price ORDER BY bus_id ASC" %(origin,destination)
		cursor = connection.cursor()
		cursor.execute(sql)
		bus_schedules = namedtuplefetchall(cursor)
		bus_schedules_check = len(bus_schedules)
		cursor.close()


		
	context = {
		"origin":origin,
		"destination":destination,
		"origins":origins,
		"origins_check":origins_check,
		"destinations":destinations,
		"destinations_check":destinations_check,
		"bus_schedules":bus_schedules,
		"bus_schedules_check":bus_schedules_check,
	}
	return render(request, "home.html", context)

@login_required(login_url='/login/')
def ticket(request, id=None):

	sql="SELECT pr.name ori_pr, pl.name ori_pl, date_time_arrive ,pr2.name des_pr, pl2.name des_pl, date_time_depart, bus_id, bc.name company, price FROM brs_cmu_bus_schedule s JOIN brs_cmu_platform pl ON pl.platform_id = s.platform_id_origin_id JOIN brs_cmu_province pr ON pr.province_id = pl.province_id_id JOIN brs_cmu_platform pl2 ON pl2.platform_id = s.platform_id_destination_id JOIN brs_cmu_province pr2 ON pr2.province_id = pl2.province_id_id JOIN brs_cmu_bus b ON b.bus_id=s.bus_id_id JOIN brs_cmu_bus_company bc ON bc.name=b.company_name_id where s.bus_schedule_id='%s'" %(id)
	cursor = connection.cursor()
	cursor.execute(sql)
	path = namedtuplefetchall(cursor)
	cursor.close()


	sql="SELECT *,EXTRACT(YEAR FROM age(date_of_birth)) AS age FROM brs_cmu_passenger WHERE user_id_id=%s" %(request.user.id)
	cursor = connection.cursor()
	cursor.execute(sql)
	users = namedtuplefetchall(cursor)
	cursor.close()

	id_card=None
	#select id_card
	for u in users:
		id_card=u.id_card

	print id_card

	if request.POST:
	 	sql="INSERT INTO brs_cmu_booking (bus_schedule_id_id,id_card_id) VALUES ('%s', '%s');" %(id,id_card)
	 	cursor = connection.cursor()
		cursor.execute(sql)
		cursor.close()
		return HttpResponseRedirect("/")
	

	context = {
		"id": id,
		"path": path,
		"users": users,
	}
	return render(request, "ticket.html", context)

@login_required(login_url='/login/')
def drivers(request):

	sql="SELECT DISTINCT bus_id_id bus_id, License,first_name,last_name,experience, EXTRACT(YEAR FROM age(date_of_birth)) as age,gender,c.name Company FROM brs_cmu_driver drver JOIN brs_cmu_drive drve ON drver.id_card = drve.id_card_id JOIN brs_cmu_bus b ON b.bus_id = drve.bus_id_id JOIN brs_cmu_bus_company c ON c.name = b.company_name_id ORDER BY bus_id_id ASC"
	cursor = connection.cursor()
	cursor.execute(sql)
	drivers = namedtuplefetchall(cursor)
	drivers_check = len(drivers)
	cursor.close()

	context = {
		"drivers": drivers,
		"drivers_check":drivers_check,
	}
	return render(request, "drivers.html", context)

@login_required(login_url='/login/')
def companys(request):

	sql="SELECT DISTINCT c.name company,COUNT(bus_id) amount_bus,phone_no FROM brs_cmu_bus b JOIN brs_cmu_bus_company c ON c.name = b.company_name_id JOIN brs_cmu_phoneno p ON p.company_name_id = c.name GROUP BY c.name,phone_no ORDER BY c.name ASC"
	cursor = connection.cursor()
	cursor.execute(sql)
	companys = namedtuplefetchall(cursor)
	companys_check = len(companys)
	cursor.close()

	context = {
		"companys": companys,
		"companys_check":companys_check,
	}
	return render(request, "companys.html", context)


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

