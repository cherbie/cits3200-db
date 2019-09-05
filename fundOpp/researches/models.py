from django.db import models
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


class ImportantDate(models.Model):
	Opportunity_ID = models.ForeignKey(Funding_Opportunity1, on_delete = models.CASCADE)
	Date_ID = models.AutoField(primary_key = True,unique = True, default = 0)
	Milestone = models.CharField(max_length = 35)
	Date = models.DateTimeField(null = False)
	Date_Status = models.CharField(max_length = 20)


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

class Funding(models.Model):
	Funding_Opportunity1= models.OneToOneField(Funding_Opportunity1, on_delete = models.CASCADE,primary_key = True,unique = True)
	Max_Amount = models.IntegerField(blank = True)
	Max_Duration = models.IntegerField(blank = True)
	Amount_Estimated = models.BooleanField(default = False )
	Duration_Estimated = models.BooleanField(default = False)