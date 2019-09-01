from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()

	#the original date the post was created auto_now_add=True (cannot be updated) - is this what we want?
	date_posted = models.DateTimeField(default=timezone.now)
	#every time the date is updated it changes - get the right timezone version??
	date_updated = models.DateTimeField(auto_now=True)

	#this is the admins job 
	#although here if the user is deleted so is the post
	#this is also a foreign key linked to all the users in the system
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	#magic method/dunder method
	#when the database is queried instead of just returning the ID it instead returns the title 
	def __str__(self):
		return self.title


