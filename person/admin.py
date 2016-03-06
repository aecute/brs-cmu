from django.contrib import admin

# Register your models here.
from .models import Passenger, Driver

class PassengerMode(admin.ModelAdmin):
	list_display = ["name", "idetificationNumber", "gender", "user_type", "id_bus"]
	#list_display_links = ["name", "id_bus", "origin", "destination"]
	#list_editable = ["title"]
	list_filter = ["name", "idetificationNumber"]

	search_fields = ["name", "idetificationNumber"]
	class Meta:
		model = Passenger

class DriverMode(admin.ModelAdmin):
	list_display = ["name", "idetificationNumber", "gender", "experience", "id_bus"]
	#list_display_links = ["name", "id_bus", "origin", "destination"]
	#list_editable = ["title"]
	list_filter = ["name", "idetificationNumber"]

	search_fields = ["name", "idetificationNumber"]
	class Meta:
		model = Driver


admin.site.register(Passenger, PassengerMode)
admin.site.register(Driver, DriverMode)



# class Passenger(models.Model):
# 	idetificationNumber = models.CharField(max_length=13, primary_key=True)
# 	name = models.CharField(max_length=40)
# 	gender = models.CharField(max_length=10)
# 	date_of_birth = models.DateField()
# 	user_type = models.CharField(max_length=20)
# 	id_bus = models.ForeignKey(Bus_schedule, default=1)

# 	def __unicode__(self):
# 		return self.name

# class Driver(models.Model):
# 	id_bus = models.ForeignKey(Bus, default=1)
# 	idetificationNumber = models.CharField(max_length=13, primary_key=True)
# 	name = models.CharField(max_length=40)
# 	gender = models.CharField(max_length=10)
# 	date_of_birth = models.DateField()
# 	experience = models.IntegerField()

# 	def __unicode__(self):
# 		return self.name