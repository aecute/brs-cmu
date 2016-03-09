from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Bus_company(models.Model):
	name = models.CharField(max_length=20, primary_key=True)
	amount_of_bus = models.IntegerField()

	def __unicode__(self):
		return self.name


class Bus(models.Model):
	bus_id = models.CharField(max_length=10, primary_key=True)
	color = models.CharField(max_length=20)
	seat = models.IntegerField()

	def __unicode__(self):
		return self.bus_id

class Bus_schedule(models.Model):
	company_name = models.ForeignKey(Bus_company, default=1)
	bus_id = models.ForeignKey(Bus, default=1)
	origin = models.CharField(max_length=40)
	destination = models.CharField(max_length=40)
	platform = models.CharField(max_length=40)
	date = models.DateTimeField()
	price = models.IntegerField()

	def __unicode__(self):
		return self.bus_id.bus_id