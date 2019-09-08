from django.db import models
import datetime

# Create your models here.
class funding_opportunity(models.Model):
	id = models.AutoField(unique = True, primary_key = True)
	name = models.CharField(max_length = 100, null = False)
	description = models.CharField(max_length = 2500,default="", null = True)
	herdc = models.IntegerField(blank = True,default = -1, null = True)
	closing_month = models.DateTimeField(null = True,default = "2019-9-8 12:00")
	creation_date = models.DateField(auto_now_add = True,null = True)
	last_updated = models.DateField(auto_now= True,null = True)
	link = models.URLField(max_length = 260,default = "", null = True)
	limit_per_uni = models.BooleanField(default = False, null = True)
	
	max_amount = models.IntegerField(default = -1,null = True)
	max_duration = models.IntegerField(default = -1,null = True)
	amount_estimated = models.BooleanField(default = False,null = True)
	duration_estimated = models.BooleanField(default = False,null = True)
	
	ecr = models.BooleanField(default = False,null = True)
	travel = models.BooleanField(default = False,null = True)
	visiting = models.BooleanField(default = False,null = True)
	wir = models.BooleanField(default = False,null = True)
	phd = models.BooleanField(default = False,null = True)
	international = models.BooleanField(default = False,null = True)
	hms = models.BooleanField(default = False,null = True)
	ems = models.BooleanField(default = False,null = True)
	science = models.BooleanField(default = False,null = True)

	
class importantdate(models.Model):
	funding_opportunity = models.ForeignKey(funding_opportunity, on_delete = models.CASCADE)
	id = models.AutoField(primary_key = True,unique = True)
	milestone = models.CharField(max_length = 35,default = "",null = True)
	date = models.DateTimeField(null = True, default = "2019-9-8 12:00")
	date_status = models.CharField(max_length = 20,default = "",null = True)