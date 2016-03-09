from django.contrib import admin

# Register your models here.
from .models import Passenger, Driver

class PassengerMode(admin.ModelAdmin):
	list_display = ["user_id", "password","name", "idetification_number", "gender"]
	#list_display_links = ["name", "id_bus", "origin", "destination"]
	#list_editable = ["title"]
	#list_filter = ["name", "idetificationNumber"]

	#search_fields = ["name", "idetificationNumber"]
	class Meta:
		model = Passenger

class DriverMode(admin.ModelAdmin):
	list_display = ["name", "idetification_number", "gender", "experience", "bus_id"]
	#list_display_links = ["name", "id_bus", "origin", "destination"]
	#list_editable = ["title"]
	#list_filter = ["name", "idetificationNumber"]

	#search_fields = ["name", "idetificationNumber"]
	class Meta:
		model = Driver


admin.site.register(Passenger, PassengerMode)
admin.site.register(Driver, DriverMode)