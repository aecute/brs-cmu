from __future__ import unicode_literals
from django.db import models

# Create your models here.
from bus.models import Bus, Bus_schedule


class Passenger(models.Model):
	id_user = models.CharField(max_length=15, primary_key=True)
	password = models.CharField(max_length=20)

	idetificationNumber = models.CharField(max_length=13)
	name = models.CharField(max_length=40)
	gender = models.CharField(max_length=10)
	date_of_birth = models.DateField()
	user_type = models.CharField(max_length=20)
	id_bus = models.ForeignKey(Bus_schedule, default=1)

	def __unicode__(self):
		return self.name

class Driver(models.Model):
	id_license = models.CharField(max_length=20, primary_key=True)
	id_bus = models.ForeignKey(Bus, default=1)
	idetificationNumber = models.CharField(max_length=13)
	name = models.CharField(max_length=40)
	gender = models.CharField(max_length=10)
	date_of_birth = models.DateField()
	experience = models.IntegerField()

	def __unicode__(self):
		return self.name



# class Bus_company(models.Model):
# 	name = models.CharField(max_length=100, primary_key=True)
# 	amount_of_bus = models.CharField(max_length=10)

# 	def __unicode__(self):
# 		return self.name


# class Bus(models.Model):
# 	id_bus = models.CharField(max_length=100, primary_key=True)
# 	color = models.CharField(max_length=100)

# 	def __unicode__(self):
# 		return self.id_bus

# class Bus_schedule(models.Model):
# 	name = models.ForeignKey(Bus_company, default=1)
# 	id_bus = models.ForeignKey(Bus, default=1)
# 	source = models.CharField(max_length=100)
# 	terminus = models.CharField(max_length=100)
# 	time = models.DateTimeField()
# 	date = models.DateField()
# 	price = models.IntegerField()

# 	def __unicode__(self):
# 		return self.source