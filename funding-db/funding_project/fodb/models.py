from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .filters import FilterManager
import datetime


class funding_opportunity(models.Model):
	year_or_month =( ('years','year'), ('months','month'),)
	herdc_type = (('1','category1'),('2','category2'),('3','category3'),('4','category4'),)

	provider = models.CharField(max_length = 100, verbose_name = 'Funding provider', default = 'please add funding provider here')
	name = models.CharField(max_length = 100, verbose_name = 'Title')
	description = models.TextField()
	herdc = models.CharField(blank = True, max_length = 15,  choices = herdc_type)
	closing_date = models.DateTimeField(null = False ,  verbose_name = 'Closing Date') #why is this called closing_month?
	creation_date = models.DateField(auto_now_add = True)
	last_updated = models.DateField(auto_now= True)
	link = models.URLField(max_length = 260)
	limit_per_uni = models.BooleanField(default = False, verbose_name = 'Limited Per University')

	max_amount = models.PositiveIntegerField(blank = True,  default = 0, verbose_name = 'Max Amount')
	max_duration = models.PositiveIntegerField(blank = True, default = 0, verbose_name = 'Duration Length')
	duration_type = models.CharField(max_length = 6, choices = year_or_month, verbose_name = 'Duration Type')
	amount_estimated = models.BooleanField(default = False )
	duration_estimated = models.BooleanField(default = False)

	ecr = models.BooleanField(default = False, verbose_name = 'ECR')
	travel = models.BooleanField(default = False, verbose_name = 'Travel')
	visiting = models.BooleanField(default = False, verbose_name = 'Visiting')
	wir = models.BooleanField(default = False, verbose_name = 'Women in Research')
	phd = models.BooleanField(default = False, verbose_name = 'PHD')
	international = models.BooleanField(default = False, verbose_name = 'International')
	hms = models.BooleanField(default = False, verbose_name = 'HMS')
	ems = models.BooleanField(default = False, verbose_name = 'EMS')
	science = models.BooleanField(default = False, verbose_name = 'Science')

	is_hidden = models.BooleanField(default = False, verbose_name = 'Hidden from regular view')

	External_deadline  = models.DateTimeField(blank = True, null = True)
	Internal_deadline = models.DateTimeField(blank = True, null = True)
	EOI_deadline  =  models.DateTimeField(blank = True, null = True, verbose_name = 'Expression of interest deadline')
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
