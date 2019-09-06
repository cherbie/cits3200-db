from django.db import models
<<<<<<< HEAD
=======
from django.utils import timezone
from django.contrib.auth.models import User
>>>>>>> 9231fdcc3a1675c3acbbe637a3362797c5c58c33
import datetime

# Create your models here.
class Funding_Opportunity1(models.Model):
	Opportunity_ID = models.AutoField(unique = True, primary_key = True,default = 0)
	Opportunity_Name = models.CharField(max_length = 100)
	Description = models.CharField(max_length = 2500)
	HERDC = models.IntegerField(blank = True)
	Closing_Month = models.DateTimeField(null = False)
	Creation_Date = models.DateTimeField(auto_now = True)
	Last_Updated = models.DateTimeField(auto_now_add = True)
	Link = models.CharField(max_length = 260)
	limit_per_uni = models.BooleanField(default = False)

<<<<<<< HEAD
	
=======
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

# Create your models here.
class Funding_Opportunity1(models.Model):
	Opportunity_ID = models.AutoField(unique = True, primary_key = True,default = 0)
	Opportunity_Name = models.CharField(max_length = 100)
	Description = models.CharField(max_length = 2500)
	HERDC = models.IntegerField(blank = True)
	Closing_Month = models.DateTimeField(null = False)
	Creation_Date = models.DateTimeField(auto_now = True)
	Last_Updated = models.DateTimeField(auto_now_add = True)
	Link = models.CharField(max_length = 260)
	limit_per_uni = models.BooleanField(default = False)


>>>>>>> 9231fdcc3a1675c3acbbe637a3362797c5c58c33
class ImportantDate(models.Model):
	Opportunity_ID = models.ForeignKey(Funding_Opportunity1, on_delete = models.CASCADE)
	Date_ID = models.AutoField(primary_key = True,unique = True, default = 0)
	Milestone = models.CharField(max_length = 35)
	Date = models.DateTimeField(null = False)
	Date_Status = models.CharField(max_length = 20)
<<<<<<< HEAD
	
	
=======


>>>>>>> 9231fdcc3a1675c3acbbe637a3362797c5c58c33
class Boolean_Tags(models.Model):
	Funding_Opportunity1= models.OneToOneField(Funding_Opportunity1, on_delete = models.CASCADE,primary_key = True,unique = True)
	ECR = models.BooleanField(default = False)
	Travel = models.BooleanField(default = False)
	Visiting = models.BooleanField(default = False)
	WiR = models.BooleanField(default = False)
	PhD = models.BooleanField(default = False)
	International = models.BooleanField(default = False)
	HMS = models.BooleanField(default = False)
	EMS = models.BooleanField(default = False)
	Science = models.BooleanField(default = False)
<<<<<<< HEAD
	
=======

>>>>>>> 9231fdcc3a1675c3acbbe637a3362797c5c58c33
class Funding(models.Model):
	Funding_Opportunity1= models.OneToOneField(Funding_Opportunity1, on_delete = models.CASCADE,primary_key = True,unique = True)
	Max_Amount = models.IntegerField(blank = True)
	Max_Duration = models.IntegerField(blank = True)
	Amount_Estimated = models.BooleanField(default = False )
<<<<<<< HEAD
	Duration_Estimated = models.BooleanField(default = False)
=======
	Duration_Estimated = models.BooleanField(default = False)
>>>>>>> 9231fdcc3a1675c3acbbe637a3362797c5c58c33
