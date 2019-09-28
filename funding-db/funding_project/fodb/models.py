from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .filters import FilterManager
import datetime


class funding_opportunity(models.Model):
	Year_or_Month =( ('Y','year'), ('M','month'),)
	Forecast_Mon = (('1','Jan'), ('2','Feb'), ('3','Mar'), ('4','Apr'), ('5','May'), ('6','Jun'), ('7','Jul'), ('8','Aug'), ('9','Sep'), ('10','Oct'), ('11','Nov'), ('12','Dec'),)

	provider = models.CharField(max_length = 100, verbose_name = 'Funding provider',default = 'none')
	name = models.CharField(max_length = 100, verbose_name = 'Title')
	description = models.CharField(max_length = 50000)
	closing_month = models.DateTimeField(null = False)
	creation_date = models.DateField(auto_now_add = True)
	last_updated = models.DateField(auto_now= True)
	link = models.URLField(max_length = 260)
	limit_per_uni = models.BooleanField(default = False, verbose_name = 'Limited Per University')

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
	hms = models.BooleanField(default = False, verbose_name = 'HMS')
	ems = models.BooleanField(default = False, verbose_name = 'EMS')
	science = models.BooleanField(default = False, verbose_name = 'SCI')
	fable = models.BooleanField(default = False, verbose_name = 'FABLE')

	is_hidden = models.BooleanField(default = False, verbose_name = 'Hidden from regular view')

	External_deadline = models.DateTimeField(blank = True, null = True)
	Forecast_Month = models.CharField(blank = True, max_length = 15,  choices = Forecast_Mon)
	Internal_deadline = models.DateTimeField(blank = True, null = True)
	EOI_deadline  = models.DateTimeField(blank = True, null = True, verbose_name = 'Expression of interest deadline')
	Minimum_data_deadline = models.DateTimeField(blank = True, null = True)


	objects = models.Manager() # default list of entries
	filters = FilterManager() # filtered list of entries
	def __str__(self):
		return self.name



	class Meta:
		ordering = ['name']
		verbose_name = 'Funding Opportunity'
		verbose_name_plural = 'Funding Opportunities'


#class fodb_date(models.Model):
#	fodb = models.ForeignKey(funding_opportunity, on_delete=models.CASCADE)
#	date = models.ForeignKey(important_date, on_delete=models.CASCADE)
#
