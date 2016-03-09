from django import forms

from .models import Passenger

class LoginForm(forms.Form):
	user_id = forms.CharField(max_length=20)
	password = forms.CharField(max_length=20, widget=forms.PasswordInput)

class RegisterForm(forms.ModelForm):

	class Meta:
		model = Passenger
		fields = [
			"user_id",
			"password",
			"idetification_number",
			"name",
			"gender",
			"date_of_birth",
		]
		widgets = {
            'password': forms.PasswordInput(),
        }
		

