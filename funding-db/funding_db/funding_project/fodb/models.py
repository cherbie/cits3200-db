from django.db import models
import datetime

# Create your models here.
class funding_opportunity(models.Model):
	id = models.AutoField(unique = True, primary_key = True)
	name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 2500)
	herdc = models.IntegerField(blank = True)
	closing_month = models.DateTimeField(null = False)
	creation_date = models.DateField(auto_now_add = True)
	last_updated = models.DateField(auto_now= True)
	link = models.URLField(max_length = 260)
	limit_per_uni = models.BooleanField(default = False)
	max_amount = models.IntegerField(blank = True)
	max_duration = models.IntegerField(blank = True)
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

	
class importantdate(models.Model):
	funding_opportunity_id = models.ForeignKey(funding_opportunity, on_delete = models.CASCADE)
	id = models.AutoField(primary_key = True,unique = True)
	milestone = models.CharField(max_length = 35)
	date = models.DateTimeField(null = False)
	date_dtatus = models.CharField(max_length = 20)