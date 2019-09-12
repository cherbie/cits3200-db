from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Post, funding_opportunity, important_date
from .forms import FilterForm
from django.db.models import Q
import time


# Create your views here.
# This is where the routes are held

def home(request):
	'''
		Rendering of fodb/home.html ... applying filter QuerySet from ./filter.py
	'''

	form = FilterForm() # manage the html options of the fields
	qs = funding_opportunity.filters.filter_qs(request) # returns filtered queryset

	return render(request, 'fodb/home.html', {'posts': qs, 'form': form})


class PostListView(ListView):
	model = funding_opportunity
	template_name = 'fodb/home.html'
	context_object_name = 'posts'
	ordering = ['-last_updated']

class PostDetailView(DetailView):
	model = funding_opportunity
	template_name = 'fodb/funding_opportunity_detail.html'



# you can change this to the welcome page?
# def about(request):
# 	return render(request,'fodb/about.html', {'title':'About'})

def error(request, error=None):
	'''
		Render the error template if an error has occured.
	'''
	if error == None:
		error = {
			'title': 'Unexpected Error',
			'status_code': 404,
			'message': 'error message.'
		}
	return render(request, 'fodb/error.html', {'error':error})


def unknown(request):
	'''
		Redirects to controlled error page.
	'''
	return redirect('/error')


def db_update(request, args, kwargs):
	'''
		View that controls the add and edit template rendering.
	'''
	db_fields = {
		"id":-1,
		'title':"Funding Opportunity",
		'description': "This is the description text",
		'date': time.asctime(),
	}
	prop = {
		"title": "Funding Opportunity Entry",
		"field": db_fields,
		"submit": "Add",
		"action": "/",
	}
	return render(request, 'fodb/db-update.html', prop)
