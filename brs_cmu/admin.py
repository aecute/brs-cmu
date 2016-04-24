from django.contrib import admin

from .models import *
# Register your models here.

class Bus_company_Admin(admin.ModelAdmin):
	class Meta:
		model = Bus_company

class Bus_Admin(admin.ModelAdmin):
	list_display = ["bus_id", "seats", "company_name"]
	class Meta:
		model = Bus

class Bus_schedule_Admin(admin.ModelAdmin):
	list_display = ["bus_schedule_id", "bus_id", "platform_id_origin", "date_time_arrive", "platform_id_destination", "date_time_depart", "price"]
	class Meta:
		model = Bus_schedule

class Province_Admin(admin.ModelAdmin):
	list_display = ["province_id", "name"]
	class Meta:
		model = Province

class Platform_Admin(admin.ModelAdmin):
	list_display = ["platform_id", "name", "province_id"]
	class Meta:
		model = Platform

class PhoneNo_Admin(admin.ModelAdmin):
	list_display = ["phone_no", "company_name"]
	class Meta:
		model = PhoneNo

class Passenger_Admin(admin.ModelAdmin):
	list_display = ["id_card", "first_name", "last_name", "gender", "date_of_birth", "phone_number", "address","user_id"]
	class Meta:
		model = Passenger

class booking_Admin(admin.ModelAdmin):
	list_display = ["id_card", "bus_schedule_id"]
	class Meta:
		model = booking

class Driver_Admin(admin.ModelAdmin):
	list_display = ["id_card", "first_name", "last_name", "gender", "date_of_birth", "license", "experience"]
	class Meta:
		model = Driver

class Drive_Admin(admin.ModelAdmin):
	list_display = ["id_card", "bus_id"]
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