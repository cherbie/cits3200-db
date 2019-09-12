from django.shortcuts import render, redirect, render_to_response
from django.views.generic import ListView, DetailView
from .models import Post, funding_opportunity, important_date
from .filters import PostFilter
import time


# Create your views here.
# This is where the routes are held

def home(request):
	'''
		Display the list of database entries.
		Render the main.html template.
	'''
	context = {
		'posts': funding_opportunity.objects.all()
	}
	return render(request,'fodb/home.html', context)

# you can change this to the welcome page?
def welcome(request):
 	return render(request,'fodb/welcome.html', {'title':'Welcome'})



def filter_request(request):
	'''
		Additional filtering service provided by django-filter.
	'''
	posts = funding_opportunity.objects.all()
	post_filter = PostFilter(request.GET, queryset=posts)
	return render(request, 'fodb/home.html', {'filter': post_filter})


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
