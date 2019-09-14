from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime


class funding_opportunity(models.Model):
	Year_or_Month =( ('Y','Year'), ('M','Month'),)
	Herdc_type = (('1','category1'),('2','category2'),('3','category3'),('4','category4'),)

	id = models.AutoField(unique = True, primary_key = True)
	name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 2500)
	herdc = models.CharField(blank = True, max_length = 15,  choices = Herdc_type)
	closing_month = models.DateTimeField(null = False, localize=True)
	creation_date = models.DateField(auto_now_add = True, localize=True)
	last_updated = models.DateField(auto_now= True, localize=True)
	link = models.URLField(max_length = 260)
	limit_per_uni = models.BooleanField(default = False)

	max_amount = models.IntegerField(blank = True)
	max_duration = models.IntegerField(blank = True)
	duration_type = models.CharField(max_length = 6, choices = Year_or_Month, default = "Month")
	amount_estimated = models.BooleanField(default = False )
	duration_estimated = models.BooleanField(default = False)

	ecr = models.BooleanField(default = False)
	travel = models.BooleanField(default = False)
	visiting = models.BooleanField(default = False)
	wir = models.BooleanField(default = False)
	phd = models.BooleanField(default = False)
	international = models.BooleanField(default = False)
	hms = models.BooleanField(default = False)
	ems = models.BooleanField(default = False)
	science = models.BooleanField(default = False)

	is_hidden = models.BooleanField(default = False)

	def __str__(self):
		return self.name


class important_date(models.Model):
	id = models.AutoField(primary_key = True,unique = True)
	milestone = models.CharField(max_length = 35)
	date = models.DateTimeField(null = False, localize=True)
	date_status = models.CharField(max_length = 20, localize=True)



class fodb_date(models.Model):
	fodb_id = models.ManyToManyField(funding_opportunity)
	date_id = models.ManyToManyField(important_date)