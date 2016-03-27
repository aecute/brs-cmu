from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from bus.models import Bus, Bus_schedule


class Passenger(models.Model):
	idetification_number = models.CharField(max_length=13, primary_key=True)
	name = models.CharField(max_length=40)
	gender = models.CharField(max_length=10)
	date_of_birth = models.DateField()
	contact = models.TextField()
	address = models.TextField()

	user_id = models.ForeignKey(User)


	def __unicode__(self):
		return self.idetification_number

class View(models.Model):
	idetification_number = models.ForeignKey(Passenger, default=1)
	bus_schedule_number = models.ForeignKey(Bus_schedule, default=1)

	def __unicode__(self):
		return self.idetification_number.idetification_number


class Driver(models.Model):
	idetification_number = models.CharField(max_length=13, primary_key=True)
	name = models.CharField(max_length=40)
	gender = models.CharField(max_length=10)
	date_of_birth = models.DateField()
	license = models.CharField(max_length=20)
	experience = models.IntegerField()

	bus_id = models.ForeignKey(Bus, default=1)

	def __unicode__(self):
		return self.idetification_number

class Drive(models.Model):
	idetification_number = models.ForeignKey(Driver, default=1)
	bus_id = models.ForeignKey(Bus, default=1)

	def __unicode__(self):
		return self.idetification_number.idetification_number