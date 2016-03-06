from django import forms

from .models import Passenger

class LoginForm(forms.ModelForm):

	# confirm_password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = Passenger
		fields = [
			"id_user",
			"password"
		]
		widgets = {
            'password': forms.PasswordInput(),
        }

class RegisterForm(forms.ModelForm):


	class Meta:
		model = Passenger
		fields = [
			"id_user",
			"password",
			"idetificationNumber",
			"name",
			"gender",
			"date_of_birth",
			"user_type",
		]
		widgets = {
            'password': forms.PasswordInput(),
        }
		


	# id_user = models.CharField(max_length=15, primary_key=True)
	# password = models.CharField(max_length=20)

	# idetificationNumber = models.CharField(max_length=13)
	# name = models.CharField(max_length=40)
	# gender = models.CharField(max_length=10)
	# date_of_birth = models.DateField()
	# user_type = models.CharField(max_length=20)
	# id_bus = models.ForeignKey(Bus_schedule, default=1)