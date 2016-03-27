from django.contrib import admin

# Register your models here.
from .models import Bus_company, Bus, Bus_schedule, PhoneNo

class Bus_companyMode(admin.ModelAdmin):
	list_display = ["name", "amount_of_bus"]
	class Meta:
		model = Bus_company

class PhoneNoMode(admin.ModelAdmin):
	list_display = ["phone_no", "company_name"]
	class Meta:
		model = PhoneNo

class Bus_Mode(admin.ModelAdmin):
	list_display = ["bus_id", "seats"]
	class Meta:
		model = Bus

class Bus_scheduleMode(admin.ModelAdmin):
	list_display = ["company_name", "bus_id", "origin", "destination", "platform", "date", "price"]
	list_display_links = ["company_name", "bus_id", "origin", "destination"]
	class Meta:
		model = Bus_schedule

admin.site.register(Bus_company, Bus_companyMode)
admin.site.register(PhoneNo, PhoneNoMode)
admin.site.register(Bus, Bus_Mode)
admin.site.register(Bus_schedule, Bus_scheduleMode)