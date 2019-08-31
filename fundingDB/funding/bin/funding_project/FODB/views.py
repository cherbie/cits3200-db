from django.shortcuts import render
from .models import Post


# Create your views here.
# This is where the routes are held 

#or make this the welcome page?
def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request,'fodb/home.html', context)



#you can change this to the welcome page?
def about(request):
	return render(request,'fodb/about.html', {'title':'About'})



