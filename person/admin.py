from django.contrib import admin

# Register your models here.
from .models import Passenger, Driver

class PassengerMode(admin.ModelAdmin):
	#list_display = ["name", "idetification_number", "gender"]

	class Meta:
		model = Passenger

	
class DriverMode(admin.ModelAdmin):
	#list_display = ["name", "idetification_number", "gender", "experience", "bus_id"]

	class Meta:
		model = Driver


admin.site.register(Passenger, PassengerMode)
admin.site.register(Driver, DriverMode)