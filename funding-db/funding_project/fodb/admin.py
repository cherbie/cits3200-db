from django.contrib import admin
from .models import  funding_opportunity, important_date
# Register your models here.

admin.site.register(funding_opportunity)
admin.site.register(important_date)

