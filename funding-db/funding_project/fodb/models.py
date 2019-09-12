from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .filters import FilterManager
import datetime

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()

	#the original date the post was created auto_now_add=True (cannot be updated) - is this what we want?
	date_posted = models.DateTimeField(default=timezone.now)
	#every time the date is updated it changes - get the right timezone version??
	date_updated = models.DateTimeField(auto_now=True)

	#this is the admins job
	#although here if the user is deleted so is the post
	#this is also a foreign key linked to all the users in the system
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	#magic method/dunder method
	#when the database is queried instead of just returning the ID it instead returns the title
	def __str__(self):
		return self.title


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

	objects = models.Manager() # default list of entries
	filters = FilterManager() # filtered list of entries

	def __str__(self):
		return self.name


class important_date(models.Model):
	funding_opportunity = models.ForeignKey(funding_opportunity, on_delete = models.CASCADE)
	id = models.AutoField(primary_key = True,unique = True)
	milestone = models.CharField(max_length = 35)
	date = models.DateTimeField(null = False)
	date_status = models.CharField(max_length = 20)
