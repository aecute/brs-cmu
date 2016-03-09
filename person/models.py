from __future__ import unicode_literals
from django.db import models

# Create your models here.
from bus.models import Bus


class Passenger(models.Model):
	user_id = models.CharField(max_length=15, primary_key=True)
	password = models.CharField(max_length=20)

	idetification_number = models.CharField(max_length=13)
	name = models.CharField(max_length=40)
	gender = models.CharField(max_length=10)
	date_of_birth = models.DateField()

	def __unicode__(self):
		return self.name


class Driver(models.Model):
	license = models.CharField(max_length=20, primary_key=True)
	bus_id = models.ForeignKey(Bus, default=1)
	idetification_number = models.CharField(max_length=13)
	name = models.CharField(max_length=40)
	gender = models.CharField(max_length=10)
	date_of_birth = models.DateField()
	experience = models.IntegerField()

	def __unicode__(self):
		return self.name