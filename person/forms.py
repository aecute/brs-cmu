from django import forms

from django.contrib.auth.models import User
from .models import Passenger


class LoginForm(forms.Form):
	user_id = forms.CharField(max_length=20)
	password = forms.CharField(max_length=20, widget=forms.PasswordInput)

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
	idetification_number = forms.CharField(widget=forms.TextInput(attrs={'size':13}))
	contact = forms.CharField(widget=forms.Textarea, required=False)
	address = forms.CharField(widget=forms.Textarea, required=False)

	class Meta:
		model = Passenger
		fields = [
			"idetification_number",
			"name",
			"gender",
			"date_of_birth",
			"contact",
			"address",
		]

