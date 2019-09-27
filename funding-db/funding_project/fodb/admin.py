from django.contrib import admin, auth
from django.contrib.auth.models import User, Group
from .models import funding_opportunity
from django.utils.html import format_html
# Register your models here.


#admin.site.register(Post)
#admin.site.register(funding_opportunity)
#admin.site.register(important_date)

admin.site.site_header = 'Funding Opportunities Database'


class FundingOpportunityAdmin(admin.ModelAdmin):
	fieldsets = [
        ('Funding Opportunity',{'fields': ['name','provider','description','link','limit_per_uni']}),
        ('Date Information', {'fields': [('closing_month','Internal_deadline'), ('EOI_deadline','Minimum_data_deadline'),('External_deadline','Forecast_Month')]}),
        ('Amount and Duration', {'fields': ['max_amount','amount_estimated','max_duration','duration_type','duration_estimated']}),
        ('Tags', {'fields': ['ecr','travel','visiting','wir','phd','international','hms','ems','science', 'fable','is_hidden' ]}),
    ]
	list_filter = ('closing_month', )
	list_display = ('name', 'closing_month','max_amount','max_duration')
	search_fields = ['description','name']

admin.site.register(funding_opportunity,FundingOpportunityAdmin)

class UserAdmin(admin.ModelAdmin):
	search_field = ('name')



admin.site.unregister(Group)