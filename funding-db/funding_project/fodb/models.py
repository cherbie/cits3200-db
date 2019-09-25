from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .filters import FilterManager
import datetime



class funding_opportunity(models.Model):
	Year_or_Month =( ('Y','year'), ('M','month'),)
	Herdc_type = (('1','category1'),('2','category2'),('3','category3'),('4','category4'),)

	provider = models.CharField(max_length = 100, verbose_name = 'Funding provider')
	name = models.CharField(max_length = 100, verbose_name = 'Title')
	description = models.CharField()
	herdc = models.CharField(blank = True, max_length = 15,  choices = Herdc_type)
	closing_month = models.DateTimeField(null = False)
	creation_date = models.DateField(auto_now_add = True)
	last_updated = models.DateField(auto_now= True)
	link = models.URLField(max_length = 260)
	limit_per_uni = models.BooleanField(default = False)

	max_amount = models.IntegerField(blank = True)
	max_duration = models.IntegerField(blank = True)
	duration_type = models.CharField(max_length = 6, choices = Year_or_Month)
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

	External_deadline = models.DateTimeField(blank = True, null = True)
	Internal_deadline = models.DateTimeField(blank = True, null = True)
	EOI_deadline  = models.DateTimeField(blank = True, null = True, verbose_name = 'Expression of interest deadline')
	Minimum_data_deadline = models.DateTimeField(blank = True, null = True)


	objects = models.Manager() # default list of entries
	filters = FilterManager() # filtered list of entries

	def __str__(self):
		return self.name



