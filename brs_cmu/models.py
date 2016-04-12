from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User

#BUS
class Bus_company(models.Model):
	name = models.CharField(max_length=20, primary_key=True)

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
	seats = models.IntegerField()
	company_name = models.ForeignKey(Bus_company, default=1)

	def __unicode__(self):
		return self.bus_id

class Province(models.Model):
	province_id = models.CharField(max_length=10, primary_key=True)
	name = models.CharField(max_length=15)

	def __unicode__(self):
		return self.province_id

class Platform(models.Model):
	platform_id = models.CharField(max_length=10, primary_key=True)
	name = models.CharField(max_length=15)
	province_id = models.ForeignKey(Province, default=1)

	def __unicode__(self):
		return self.platform_id


class Bus_schedule(models.Model):
	bus_schedule_id = models.CharField(max_length=10, primary_key=True)
	bus_id = models.ForeignKey(Bus, default=1)
	platform_id_origin = models.ForeignKey(Platform, related_name='arrive', default=1)
	date_time_arrive = models.DateTimeField()
	platform_id_destination = models.ForeignKey(Platform, related_name='depart', default=1)
	date_time_depart = models.DateTimeField()
	price = models.IntegerField()

	def __unicode__(self):
		return self.bus_schedule_id


#SERVICE
class Passenger(models.Model):
	id_card = models.CharField(max_length=13, primary_key=True)
	first_name = models.CharField(max_length=15)
	last_name = models.CharField(max_length=15)
	gender = models.CharField(max_length=10)
	date_of_birth = models.DateField()
	phone_number = models.CharField(max_length=10)
	address = models.TextField()

	user_id = models.ForeignKey(User)


	def __unicode__(self):
		return self.id_card

class booking(models.Model):
	id_card = models.ForeignKey(Passenger, default=1)
	bus_schedule_id = models.ForeignKey(Bus_schedule, default=1)

	def __unicode__(self):
		return self.id_card.id_card


class Driver(models.Model):
	id_card = models.CharField(max_length=13, primary_key=True)
	first_name = models.CharField(max_length=15)
	last_name = models.CharField(max_length=15)
	gender = models.CharField(max_length=10)
	date_of_birth = models.DateField()
	license = models.CharField(max_length=20)
	experience = models.IntegerField()

	def __unicode__(self):
		return self.id_card

class Drive(models.Model):
	id_card = models.ForeignKey(Driver, default=1)
	bus_id = models.ForeignKey(Bus, default=1)

	def __unicode__(self):
		return self.id_card.id_card