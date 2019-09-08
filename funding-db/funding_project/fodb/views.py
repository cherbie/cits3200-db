from django.shortcuts import render, redirect
from .models import Post, Funding_Opportunity1
import time


# Create your views here.
# This is where the routes are held

def home(request):
	'''
		Display the list of database entries.
		Render the main.html template.
	'''
	context = {
		'posts': Post.objects.all()
	}
	return render(request,'fodb/home.html', context)


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
