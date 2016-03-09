from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from .models import Passenger
from .forms import LoginForm, RegisterForm

def login(request):
	users = Passenger.objects.all()

	form = LoginForm(request.POST or None)
	if form.is_valid():
		user_id = form.cleaned_data['user_id']
		password = form.cleaned_data['password']

		for user in users:
			if(user.user_id == user_id and user.password == password):
				print "user id : " + user_id + " had logined."
				context = {
					"user_id": user_id
				}
				return render(request, "reservation.html", context)
		
	context = {
		"form": form
	}
	return render(request, "login.html", context)

def register(request):
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		regis = form.save(commit=False)
		regis.save()
		return HttpResponseRedirect("/")


	context = {
		"form": form
	}
	return render(request, "register.html", context)

def reservation(request):
	user_id = "test"
	context = {
		"user_id": user_id
	}
	return render(request, "reservation.html", context)

