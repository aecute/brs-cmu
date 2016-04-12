from django import forms

from django.contrib.auth.models import User
from .models import Passenger


class LoginForm(forms.Form):
	username = forms.CharField(max_length=30)
	password = forms.CharField(max_length=30, widget=forms.PasswordInput)

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = [
			"username",
			"email",
			"password",
		]



class UserDetailForm(forms.ModelForm):
	id_card=forms.CharField(max_length=13, min_length=13)

	gender_choices = (('m', 'Male'),('f', 'Female'),)
	gender = forms.ChoiceField(choices=gender_choices)
	
	phone_number = forms.CharField(widget=forms.TextInput, required=False)
	address = forms.CharField(widget=forms.Textarea, required=False)
	date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))    

	class Meta:
		model = Passenger
		fields = [
			"id_card",
			"first_name",
			"last_name",
			"gender",
			"date_of_birth",
			"phone_number",
			"address",
		]
