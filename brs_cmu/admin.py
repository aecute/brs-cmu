from django.contrib import admin

from .models import *
# Register your models here.

class Bus_company_Admin(admin.ModelAdmin):
	#list_display = ["company_name", "bus_id", "origin", "destination", "platform", "date", "price"]
	#list_display_links = ["company_name", "bus_id", "origin", "destination"]
	class Meta:
		model = Bus_company

class Bus_Admin(admin.ModelAdmin):
	#list_display = ["company_name", "bus_id", "origin", "destination", "platform", "date", "price"]
	#list_display_links = ["company_name", "bus_id", "origin", "destination"]
	class Meta:
		model = Bus

class Bus_schedule_Admin(admin.ModelAdmin):
	#list_display = ["company_name", "bus_id", "origin", "destination", "platform", "date", "price"]
	#list_display_links = ["company_name", "bus_id", "origin", "destination"]
	class Meta:
		model = Bus_schedule

class Province_Admin(admin.ModelAdmin):
	#list_display = ["company_name", "bus_id", "origin", "destination", "platform", "date", "price"]
	#list_display_links = ["company_name", "bus_id", "origin", "destination"]
	class Meta:
		model = Province

class Platform_Admin(admin.ModelAdmin):
	#list_display = ["company_name", "bus_id", "origin", "destination", "platform", "date", "price"]
	#list_display_links = ["company_name", "bus_id", "origin", "destination"]
	class Meta:
		model = Platform

class PhoneNo_Admin(admin.ModelAdmin):
	#list_display = ["company_name", "bus_id", "origin", "destination", "platform", "date", "price"]
	#list_display_links = ["company_name", "bus_id", "origin", "destination"]
	class Meta:
		model = PhoneNo

class Passenger_Admin(admin.ModelAdmin):
	#list_display = ["company_name", "bus_id", "origin", "destination", "platform", "date", "price"]
	#list_display_links = ["company_name", "bus_id", "origin", "destination"]
	class Meta:
		model = Passenger

class booking_Admin(admin.ModelAdmin):
	#list_display = ["company_name", "bus_id", "origin", "destination", "platform", "date", "price"]
	#list_display_links = ["company_name", "bus_id", "origin", "destination"]
	class Meta:
		model = booking

class Driver_Admin(admin.ModelAdmin):
	#list_display = ["company_name", "bus_id", "origin", "destination", "platform", "date", "price"]
	#list_display_links = ["company_name", "bus_id", "origin", "destination"]
	class Meta:
		model = Driver

class Drive_Admin(admin.ModelAdmin):
	#list_display = ["company_name", "bus_id", "origin", "destination", "platform", "date", "price"]
	#list_display_links = ["company_name", "bus_id", "origin", "destination"]
	class Meta:
		model = Drive


admin.site.register(Bus_company, Bus_company_Admin)
admin.site.register(Bus, Bus_Admin)
admin.site.register(Bus_schedule, Bus_schedule_Admin)
admin.site.register(Province, Province_Admin)
admin.site.register(Platform, Platform_Admin)
admin.site.register(PhoneNo, PhoneNo_Admin)
admin.site.register(Passenger, Passenger_Admin)
admin.site.register(booking, booking_Admin)
admin.site.register(Driver, Driver_Admin)
admin.site.register(Drive, Drive_Admin)