from django.shortcuts import render

# Create your views here.

from .forms import LoginForm, RegisterForm

def login(request):
	form = LoginForm(request.POST or None)

	context = {
		"form": form
	}
	return render(request, "login.html", context)

def register(request):
	form = RegisterForm(request.POST or None)

	context = {
		"form": form
	}
	return render(request, "register.html", context)
