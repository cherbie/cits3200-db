import csv
from django.contrib import admin, auth
from django.http import HttpResponse
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
    actions = ['make_hidden', 'make_unhidden', 'export_funding_opportunity']

    def make_hidden(self, request, queryset):
        for funding_opportunity in queryset:
            funding_opportunity.is_hidden = True
            funding_opportunity.save()

    make_hidden.short_description = 'Hide Opportunity'

    def make_unhidden(self, request, queryset):
        for funding_opportunity in queryset:
            funding_opportunity.is_hidden = False
            funding_opportunity.save()

    make_unhidden.short_description = 'Unhide Opportunity'

    def export_funding_opportunity(modeladmin, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="funding_opportunities.csv"'
        writer = csv.writer(response)
        writer.writerow(['Title', 'Funding Provider', 'Description', 'Link', 'Limited per University', 'Closing Date', 'EOI deadline' , 'Internal Deadline',
            'External Deadline', 'Minimum Data Deadline' , 'Forecast Month' , 'Max Amount' , 'Amount Estimated', 'Max Duration','Duration Type', 'Duration Estimated', 'ECR',
            'Travel','Visiting','Women In Research','PhD','International','HMS','EMS','Science','FABLE'  ])
        FO = queryset.values_list('name', 'provider', 'description', 'link', 'limit_per_uni', 'closing_date', 'EOI_deadline','Internal_deadline','External_deadline','Minimum_data_deadline',
            'Forecast_Month','max_amount','amount_estimated','max_duration','duration_type','duration_estimated','ecr','travel','visiting','wir','phd','international','hms','ems','science','fable')
        for funding_opportunity in FO:
            writer.writerow(funding_opportunity)
        return response

    export_funding_opportunity.short_description = 'Export to csv'


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


