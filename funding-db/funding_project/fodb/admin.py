from django.contrib import admin, auth
from django.contrib.auth.models import User, Group
from .models import funding_opportunity, important_date
from django.utils.html import format_html
# Register your models here.


#admin.site.register(Post)
#admin.site.register(funding_opportunity)
#admin.site.register(important_date)

admin.site.site_header = 'Funding Opportunities Database'

class important_dateInline(admin.TabularInline):
    model = important_date
    extra = 1


class FundingOpportunityAdmin(admin.ModelAdmin):
	fieldsets = [
        ('Funding Opportunity',{'fields': [('name','is_hidden'),'description','link','herdc','limit_per_uni']}),
        ('Date Information', {'fields': ['closing_date']}),
        ('Amount and Duration', {'fields': [('max_amount','amount_estimated'),('max_duration','duration_estimated') ,'duration_type']}),
        ('Tags', {'fields': ['ecr','travel','visiting','wir','phd','international','hms','ems','science' ]}),
    ]
	inlines = [important_dateInline]
	list_filter = ('closing_date', )
	list_display = ('name', 'closing_date','max_amount','max_duration')
	search_fields = ['description','name']


admin.site.register(funding_opportunity,FundingOpportunityAdmin)




admin.site.unregister(Group)