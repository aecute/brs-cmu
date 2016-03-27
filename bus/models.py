from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Bus_company(models.Model):
	name = models.CharField(max_length=20, primary_key=True)
	amount_of_bus = models.IntegerField()

	def __unicode__(self):
		return self.name

class PhoneNo(models.Model):
	phone_no = models.CharField(max_length=10)
	company_name = models.ForeignKey(Bus_company, default=1)

	class Meta:
		unique_together = ('phone_no', 'company_name')
		
	def __unicode__(self):
		return self.phone_no
		

class Bus(models.Model):
	bus_id = models.CharField(max_length=10, primary_key=True)
	reserve_seat = models.IntegerField(blank=True, null=True)
	seats = models.IntegerField()
	company_name = models.ForeignKey(Bus_company, default=1)

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

	
	class Meta:
		unique_together = ('company_name', 'bus_id')

	def __unicode__(self):
		return str(self.id)