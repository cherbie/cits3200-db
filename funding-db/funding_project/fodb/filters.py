from django.db.models import Q
from django.db import models

class FilterManager(models.Manager):
	'''
        Customly manage filters.
	'''
	fields = ['hms','ems','science','travel','ecr','international','wir','phd','visiting']

	def filter_qs(self, request):
		"""
			@return QuerySet containing all fields with specified values.
			@param HttpRequest object
		"""

		dict = request.GET.dict() # request paramaters
		q = None # models.Q object
		print(dict)
		if len(dict) == 0 :
			return super().get_queryset()

		print(self.ems_select())
		print(self.fields[0])
		if dict.__contains__(self.fields[0]):
			if q == None:
				q = self.hms_select()
			else:
				q = q | self.hms_select()
			print(q)
		if dict.__contains__(self.fields[1]):
			if q == None:
				q = self.ems_select()
			else:
				q = q | self.ems_select()
		if dict.__contains__(self.fields[2]):
			if q == None:
				q = self.science_select()
			else:
				q = q | self.science_select()
			print(q)
		if dict.__contains__(self.fields[3]):
			if q == None:
				q = self.travel_select()
			else:
				q = q | self.travel_select()
		if dict.__contains__(self.fields[4]):
			if q == None:
				q = self.ecr_select()
			else:
				q = q | self.ecr_select()
		if dict.__contains__(self.fields[5]):
			if q == None:
				q = self.international_select()
			else:
				q = q | self.international_select()
		if dict.__contains__(self.fields[6]):
			if q == None:
				q = self.wir_select()
			else:
				q = q | self.wir_select()
		if dict.__contains__(self.fields[7]):
			if q == None:
				q = self.phd_select()
			else:
				q = q | self.phd_select()
		if dict.__contains__(self.fields[8]):
			if q == None:
				q = self.visiting_select()
			else:
				q = q | self.visiting_select()
		return super().get_queryset().filter(q);

	def hms_select(self):
		print("entered")
		return Q(hms='True')

	def ems_select(self):
		return Q(ems='True')

	def science_select(self):
		return Q(science='True')

	def travel_select(self):
		return Q(travel='True')

	def ecr_select(self):
		return Q(ecr='True')

	def international_select(self):
		return Q(international='True')

	def wir_select(self):
		return Q(wir='True')

	def phd_select(self):
		return Q(phd='True')

	def visiting_select(self):
		return Q(visiting='True')
