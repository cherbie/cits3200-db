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
		self.request = request
		dict = request.GET.dict() # request paramaters
		tags = None # models.Q object
		faculty =  None
		print(dict)

		print(self.ems_select())
		print(self.fields[0])
		if dict.__contains__(self.fields[0]):
			if faculty == None:
				faculty = self.hms_select()
			else:
				faculty = faculty & self.hms_select()
			print(faculty)
		if dict.__contains__(self.fields[1]):
			if faculty == None:
				faculty = self.ems_select()
			else:
				faculty = faculty & self.ems_select()
		if dict.__contains__(self.fields[2]):
			if faculty == None:
				faculty = self.science_select()
			else:
				faculty = faculty & self.science_select()
			print(faculty)
		if dict.__contains__(self.fields[3]):
			if tags == None:
				tags = self.travel_select()
			else:
				tags = tags | self.travel_select()
		if dict.__contains__(self.fields[4]):
			if tags == None:
				tags = self.ecr_select()
			else:
				tags = tags | self.ecr_select()
		if dict.__contains__(self.fields[5]):
			if tags == None:
				tags = self.international_select()
			else:
				tags = tags | self.international_select()
		if dict.__contains__(self.fields[6]):
			if tags == None:
				tags = self.wir_select()
			else:
				tags = tags | self.wir_select()
		if dict.__contains__(self.fields[7]):
			if tags == None:
				tags = self.phd_select()
			else:
				tags = tags | self.phd_select()
		if dict.__contains__(self.fields[8]):
			if tags == None:
				tags = self.visiting_select()
			else:
				tags = tags | self.visiting_select()

		# -- RETURN STATEMENTS --
		if tags is None and faculty is None:
			return self.set_order(super().get_queryset())
		elif tags is None:
			return self.set_order(super().get_queryset().filter(faculty))
		elif faculty is None:
			return self.set_order(super().get_queryset().filter(tags))
		else:
			return self.set_order(super().get_queryset().filter(tags & faculty))

	def set_order(self, queryset):
		'''
			Responsible for ordering the resulting queryset.
			@return queryset
		'''
		str = self.request.GET.get('sort')
		if str == 'desc':
			queryset = queryset.order_by('-name')
		elif str == 'close-asc':
			queryset = queryset.order_by('closing_date')
		elif str == 'close-desc':
			queryset = queryset.order_by('-closing_date')
		else:
			queryset = queryset.order_by('name')
		print(str)
		return queryset

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
