from django.shortcuts import render, redirect
from .models import Post


# Create your views here.
# This is where the routes are held

def research(request):
	return render(request, 'fodb/tables.html')

def opportunities(request):
	'''
		Display the list of database entries.
		Render the main.html template.
	'''
	context = {
		'posts': Post.objects.all()
	}
	return render(request,'fodb/opportunities.html', context)


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
