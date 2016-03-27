from django.contrib import admin

# Register your models here.
from .models import Passenger, Driver, View, Drive

class PassengerMode(admin.ModelAdmin):
	list_display = ["user_id", "name", "idetification_number", "gender", "date_of_birth", "contact", "address"]

	class Meta:
		model = Passenger

	
class DriverMode(admin.ModelAdmin):
	list_display = ["bus_id", "name", "idetification_number", "gender", "date_of_birth", "license", "experience"]

	class Meta:
		model = Driver

class ViewMode(admin.ModelAdmin):
	list_display = ["idetification_number"]

	class Meta:
		model = View		

class DriveMode(admin.ModelAdmin):
	list_display = ["idetification_number"]

	class Meta:
		model = Drive

admin.site.register(Passenger, PassengerMode)
admin.site.register(Driver, DriverMode)
admin.site.register(View, ViewMode)
admin.site.register(Drive, DriveMode)