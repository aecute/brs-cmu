from django.contrib import admin

# Register your models here.
from .models import Bus_company, Bus, Bus_schedule

class Bus_companyMode(admin.ModelAdmin):
	list_display = ["name", "amount_of_bus"]
	#list_display_links = ["name", "id_bus", "origin", "destination"]
	#list_editable = ["title"]
	#list_filter = ["name"]

	#search_fields = ["name"]
	class Meta:
		model = Bus_company

class Bus_Mode(admin.ModelAdmin):
	list_display = ["bus_id", "color", "seat"]
	#list_display_links = ["id_bus", "color", "seat"]
	#list_editable = ["title"]
	#list_filter = ["bus_id"]

	#search_fields = ["bus_id"]
	class Meta:
		model = Bus

class Bus_scheduleMode(admin.ModelAdmin):
	list_display = ["company_name", "bus_id", "origin", "destination", "platform", "date", "price"]
	list_display_links = ["company_name", "bus_id", "origin", "destination"]
	#list_editable = ["title"]
	#list_filter = ["date"]

	#search_fields = ["origin", "destination"]
	class Meta:
		model = Bus_schedule

admin.site.register(Bus_company, Bus_companyMode)
admin.site.register(Bus, Bus_Mode)
admin.site.register(Bus_schedule, Bus_scheduleMode)




# class Bus_company(models.Model):
# 	name = models.CharField(max_length=20, primary_key=True)
# 	amount_of_bus = models.IntegerField()

# 	def __unicode__(self):
# 		return self.name


# class Bus(models.Model):
# 	id_bus = models.CharField(max_length=10, primary_key=True)
# 	color = models.CharField(max_length=20)
# 	seat = models.IntegerField()

# 	def __unicode__(self):
# 		return self.id_bus

# class Bus_schedule(models.Model):
# 	name = models.ForeignKey(Bus_company, default=1)
# 	id_bus = models.ForeignKey(Bus, default=1)
# 	origin = models.CharField(max_length=40)
# 	destination = models.CharField(max_length=40)
# 	platform = models.CharField(max_length=40)
# 	date = models.DateTimeField()
# 	price = models.IntegerField()

# 	def __unicode__(self):
# 		return self.id_bus.id_bus


