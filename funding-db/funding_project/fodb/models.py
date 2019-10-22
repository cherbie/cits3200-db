from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .filters import FilterManager
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError

'''

    THE FOLLOWING IS THE DATABASE ASSOCIATED WITH THIS WEBSITE 


'''

class funding_opportunity(models.Model):
	Year_or_Month =( ('Y','year'), ('M','month'),)
	Forecast_Mon = (('1','Jan'), ('2','Feb'), ('3','Mar'), ('4','Apr'), ('5','May'), ('6','Jun'), ('7','Jul'), ('8','Aug'), ('9','Sep'), ('10','Oct'), ('11','Nov'), ('12','Dec'),)

	provider = models.CharField(max_length = 100, verbose_name = 'Funding provider',default = '')
	name = models.CharField(max_length = 100, verbose_name = 'Title')
	description = models.TextField()
	external_submission_date = models.DateTimeField(null = False, verbose_name = 'External Submission Date')
	creation_date = models.DateField(auto_now_add = True)
	last_updated = models.DateField(auto_now= True)
	link = models.URLField(max_length = 260, verbose_name = 'Link')
	limit_per_uni = models.BooleanField(default = False, verbose_name = 'Limited Per University')


	max_amount = models.IntegerField(blank = True, null = True, verbose_name = 'Max Amount')
	max_duration = models.IntegerField(blank = True, null = True, verbose_name = 'Max Duration')
	duration_type = models.CharField(blank = True, null = True, max_length = 6, choices = Year_or_Month)
	amount_estimated = models.BooleanField(default = False )
	duration_estimated = models.BooleanField(default = False)

	ecr = models.BooleanField(default = False, verbose_name = 'Early Career Research')
	travel = models.BooleanField(default = False)
	visiting_fellow = models.BooleanField(default = False, verbose_name = 'Visiting Fellow')
	wir = models.BooleanField(default = False, verbose_name = 'Women in Research')
	phd = models.BooleanField(default = False, verbose_name= 'PhD')
	international = models.BooleanField(default = False)

	hms = models.BooleanField(default = False, verbose_name = 'Health and Medical Science')
	ems = models.BooleanField(default = False, verbose_name = 'Engineering and Mathematical Sciences')
	science = models.BooleanField(default = False, verbose_name = 'Science')
	fable = models.BooleanField(default = False, verbose_name = 'Faculty of Arts, Business, Law and Education')

	is_visible = models.BooleanField(default = True, verbose_name = 'Visible in regualar view')

	application_open_date = models.DateTimeField(blank = True, null = True, verbose_name = 'Application Open Date')
	forecast_month = models.CharField(blank = True, max_length = 15, null = True, choices = Forecast_Mon, verbose_name ='Forecast Month')
	internal_submission_date = models.DateTimeField(blank = True, null = True, verbose_name = 'Internal deadline')
	eoi_deadline  = models.DateTimeField(blank = True, null = True, verbose_name = 'Expression of interest deadline')
	minimum_data_deadline = models.DateTimeField(blank = True, null = True, verbose_name ='Minimum data deadline' )


	objects = models.Manager() # default list of entries
	filters = FilterManager() # filtered list of entries

	#CHECKS WETHER THE USER HAS ALSO TYPED IN THE DURATION TYPE WHEN ENTERING A DURATION 
	def clean(self):
		if self.max_duration is not None and self.duration_type is None:
			raise ValidationError('You have entered a max duration so you must enter duration type')	

	def __str__(self):
		return self.name



	class Meta:
		ordering = ['name']
		verbose_name = 'Funding Opportunity'
		verbose_name_plural = 'Funding Opportunities'



