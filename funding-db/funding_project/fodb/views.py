
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, render_to_response

from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.core.paginator import Paginator
from django.db import connections, connection

from .models import funding_opportunity, important_date
from .forms import FilterForm
from .modelForm import funding_opportunityForm, important_dateForm
import time


# Create your views here.
# This is where the routes are held

def opp(request):
	context = {"test": "afdsabfvadshivabdsvias"}
	display = funding_opportunity.objects.all().values()

	researches = []

	for research in display:
		researches.append(research)

	context["researches"] = researches

	print("Here\n")
	print(researches)
	return render(request, 'fodb/tables.html', context)

@login_required(login_url='login')
def home(request):
	'''
		Rendering of fodb/home.html ... applying filter QuerySet from ./filter.py
	'''
	form = FilterForm() # manage the html options of the fields
	qs = funding_opportunity.filters.filter_qs(request) # returns filtered queryset
	paginator = Paginator(qs, 25) # Show 25 contacts per page
	page = request.GET.get('page')
	display = paginator.get_page(page)

	return render(request, 'fodb/home.html', {'posts': display, 'form': form})

@login_required(login_url='login')
def details(request, pk):
	opp = funding_opportunity.objects.get(id=pk)
	return render(request, 'fodb/details.html', {'opp':opp})

# you can change this to the welcome page?
def welcome(request):
 	return render(request,'fodb/welcome.html', {'title':'Welcome'})



class PostListView(ListView):
	model = funding_opportunity
	template_name = 'fodb/home.html'
	context_object_name = 'posts'
	ordering = ['-last_updated']

class PostDetailView(DetailView):
	model = funding_opportunity
	template_name = 'fodb/funding_opportunity_detail.html'


def error(request, error=None):
	'''
		Render the error template if an error has occured.
	'''
	if error == None:
		error = {
			'title': 'Sorry this web-page cannot be found :(',
			'status_code': 404,
			'message': 'Please double check your url.'
		}
	return render(request, 'fodb/error.html', {'error':error})


def unknown(request):
	'''
		Redirects to controlled error page.
	'''
	return redirect('/error')


@login_required(login_url='login')
def db_update(request, args, kwargs):
	'''
		View that controls the add and edit template rendering.
	'''
	db_fields = {
		"id": -1,
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
