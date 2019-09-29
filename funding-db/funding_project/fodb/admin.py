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
        ('Funding Opportunity',{'fields': [('name','is_hidden'),'provider','description','link','limit_per_uni']}),
        ('Date Information', {'fields': [('closing_date', 'Internal_deadline'),('EOI_deadline','Minimum_data_deadline'),('External_deadline','Forecast_Month')]}),
        ('Amount and Duration', {'fields': [('max_amount','amount_estimated'),('max_duration','duration_estimated') ,'duration_type']}),
        ('Tags', {'fields': ['ecr','travel','visiting','wir','phd','international']}),
        ('Faculty',{'fields': ['hms','ems','science','fable']}),
    ]
    list_filter = ('closing_date', )
    list_display = ('name', 'closing_date','max_amount','max_duration', 'is_hidden')
    search_fields = ['description','name']


    # this changes the title at /admin/fodb/funding_opportunity/ 
    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': 'Select Funding Opportunity to edit'}
        return super(FundingOpportunityAdmin, self).changelist_view(request, extra_context=extra_context)

    
    
    # this changes the title at /admin/fodb/funding_opportunity/6/change/
    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        response = super(FundingOpportunityAdmin, self).render_change_form(request, context, add, change, form_url, obj)
        response.context_data['title'] = "Edit Funding Opportunity" if response.context_data['object_id'] else "Add Funding Opportunity"
        return response

admin.site.index_title = 'Funding Opportunities Administration'
admin.site.site_title = 'FODB Admin'

admin.site.register(funding_opportunity,FundingOpportunityAdmin)




admin.site.unregister(Group)


