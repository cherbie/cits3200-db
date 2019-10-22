from django.db.models import Q
from django.db import models

class FilterManager(models.Manager):
	'''
        Customly manage filters.
	'''
	fields = ['hms','ems','science','travel','ecr','international','wir','phd','visiting_fellow', 'fable', 'month', 'search']

	def search_qs(self, dict):
		'''
		   Filters the queryset based on the keywords provided in the search bar 'GET' request
		   @param dict dictionary of 'GET' method paramaters
		'''
		if not dict.__contains__('search'):
			return super().get_queryset() # no search filters applied

		text = dict.__getitem__('search') # search query
		keywords = text.split(' ');
		Qobject = None
		for word in keywords: # cycle through keywords
			if Qobject is None:
				Qobject = self.keyword_name(word) | self.keyword_desc(word) | self.keyword_provider(word)
			else:
				Qobject |= self.keyword_name(word) | self.keyword_desc(word) | self.keyword_provider(word)

		queryset = super().get_queryset().filter(Qobject); # filtered queryset

		return queryset # revised queryset


	def filter_qs(self, request):
		"""
			@return QuerySet containing all fields with specified values.
			@param HttpRequest object
		"""
		self.request = request
		dict = request.GET.dict() # request paramaters

		queryset = self.search_qs(dict); # call function to filter search keywords

		tags = None # models.Q object
		faculty =  None # models.Q object

		if dict.__contains__(self.fields[0]):
			if faculty == None:
				faculty = self.hms_select()
			else:
				faculty = faculty & self.hms_select()
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
		if dict.__contains__(self.fields[10]):
			if dict.__getitem__(self.fields[10]) == '-1':
				faculty = faculty
			elif faculty == None:
				faculty = self.month_select(dict.__getitem__(self.fields[9]))
			else:
				faculty = faculty & self.month_select(dict.__getitem__(self.fields[9]))

		# -- OR results --
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
		if dict.__contains__(self.fields[9]):
			if tags == None:
				tags = self.fable_select()
			else:
				tags = tags | self.fable_select()


		# -- RETURN STATEMENTS --
		if tags is None and faculty is None:
			return self.set_order(queryset)
		elif tags is None:
			return self.set_order(queryset.filter(faculty))
		elif faculty is None:
			return self.set_order(queryset.filter(tags))
		else:
			return self.set_order(queryset.filter(tags & faculty))

	def set_order(self, queryset):
		'''
			Responsible for ordering the resulting queryset.
			@return queryset
		'''
		str = self.request.GET.get('sort')
		if str == 'desc':
			queryset = queryset.order_by('-name')
		elif str == 'asc':
			queryset = queryset.order_by('name')
		elif str == 'close-desc':
			queryset = queryset.order_by('-external_submission_date')
		else:
			queryset = queryset.order_by('external_submission_date')

		return queryset

	def keyword_name(self, keyword):
		return Q(name__icontains=keyword)

	def keyword_desc(self, keyword):
		return Q(description__icontains=keyword)

	def keyword_provider(self, keyword):
		return Q(provider__icontains=keyword)

	def hms_select(self):
		return Q(hms='True')

	def ems_select(self):
		return Q(ems='True')

	def science_select(self):
		return Q(science='True')

	def fable_select(self):
		return Q(fable='True')

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
		return Q(visiting_fellow='True')

	def month_select(self, month):
		return Q(Forecast_Mon = month)
