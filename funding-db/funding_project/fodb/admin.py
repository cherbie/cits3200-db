import csv
from django.contrib import admin, auth
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from import_export import fields, resources, results, widgets
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from .models import funding_opportunity
from django.utils.html import format_html
from django.utils import timezone
from import_export.formats import base_formats
import datetime 
import codecs
from django.conf import settings
from django.contrib.admin import widgets
from daterange_filter.filter import DateRangeFilter
from .forms import NewAdminForm


'''

    THE FOLLOWING CODE IS RESPONSIBLE FOR THE ADMINISTRATION VIEW IN THE APP
    IT BUILDS ONTOP ON DJANGO FEATURES 


'''


admin.site.site_header = 'Funding Opportunities Database'



#THE FOLLOWING CLASS IS RESPONSIBLE FOR THE IMPORT/EXPORT FEATURE IN THE ADMIN VIEW
class FODBResource(resources.ModelResource):
    class Meta:
        model = funding_opportunity
        exclude = ('creation_date')

        export_order = ('id','name', 'provider', 'description', 'link', 'limit_per_uni',
            'external_submission_date', 'eoi_deadline','internal_submission_date','application_open_date','minimum_data_deadline','forecast_month',
            'max_amount','amount_estimated','max_duration','duration_type','duration_estimated',
            'ecr','travel','visiting_fellow','wir','phd','international','hms','ems','science','fable', 'is_visible')

        fields = ('id','name', 'provider', 'description', 'link', 'limit_per_uni',
            'external_submission_date', 'eoi_deadline','internal_submission_date','application_open_date','minimum_data_deadline','forecast_month',
            'max_amount','amount_estimated','max_duration','duration_type','duration_estimated',
            'ecr','travel','visiting_fellow','wir','phd','international','hms','ems','science','fable', 'is_visible')
        
        #THIS FORMATS THE DATES FRO READABILITY
        widgets = {
                'external_submission_date': {'format': '%d-%m-%Y %H:%M'},
                'eoi_deadline': {'format': '%d-%m-%Y %H:%M'},
                'internal_submission_date': {'format': '%d-%m-%Y %H:%M'},
                'application_open_date': {'format': '%d-%m-%Y %H:%M'},
                'minimum_data_deadline': {'format': '%d-%m-%Y %H:%M'},

                }

class FundingOpportunityAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = FODBResource
    form = NewAdminForm

    #THIS FORMATS THE FORM USED TO TO ADD A FUNDING OPPORTUNITY
    fieldsets = [
        ('Funding Opportunity',{'fields': [('name','is_visible'),'provider','description','link','limit_per_uni']}),
        ('Date Information', {'fields': [('external_submission_date', 'forecast_month'),('eoi_deadline','minimum_data_deadline'),('application_open_date','internal_submission_date')]}),
        ('Amount and Duration', {'fields': [('max_amount','amount_estimated'),('max_duration','duration_estimated') ,'duration_type']}),
        ('Tags', {'fields': ['ecr','travel','visiting_fellow','wir','phd','international']}),
        ('Faculty',{'fields': ['hms','ems','science','fable']}),
    ]

    #IN THE VIEW THAT CONTAINS THE FUNDING OPPORTUNITIES THESE ARE THE FILTERS FOUND ON THE RIGHT-HAND SIDE 
    #date_hierarchy = 'external_submission_date'
    list_filter = ('external_submission_date',
        'forecast_month',
    )

    #THE FUNNDING OPPORTUNITIES ARE SHOW WITH THE FOLLOWING CRITERIA 
    list_display = ('name', 'external_submission_date','max_amount','max_duration','is_visible', 'forecast_month')

    #THE TABLE CAN BE SEARCHED BY THE FOLLOWING CRITERIA
    search_fields = ['description','name', 'provider']

    #THESE ARE THE ACTIONS THAT CAN BE PLACES ON THE TABLE - THE FUNCTIONS ASSOCIATED WITH THE ACTIONS ARE DESCRIBED BELOW
    actions = ['make_hidden', 'make_unhidden', 'export_funding_opportunity','dateformat','update_expired']

    #THIS FUNCTION HIDES ANY EXPIRED OPPORTUNITIES VALUES 
    def update_expired(self, request, queryset):
        for funding_opportunity in queryset:
            if funding_opportunity.external_submission_date < timezone.now():
                funding_opportunity.is_visible = False
                funding_opportunity.save()
    update_expired.short_description = 'Hide expired opportunities'

    #THIS FUNCTION HIDES THE SELECTED OPPORTUNITIES VALUES 
    def make_hidden(self, request, queryset):
        for funding_opportunity in queryset:
            funding_opportunity.is_visible = False
            funding_opportunity.save()

    make_hidden.short_description = 'Hide Opportunity'

    #THIS FUNCTION UNHIDES THE SELECTED OPPORTUNITIES VALUES 
    def make_unhidden(self, request, queryset):
        for funding_opportunity in queryset:
            funding_opportunity.is_visible = True
            funding_opportunity.save()
    make_unhidden.short_description = 'Unhide Opportunity'


    #THIS FUNCTION ADDS THE ABBILITY TO EXPORT SELECTED FUNDING OPPORTUNITIES TO CSV
    def export_funding_opportunity(modeladmin, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="selected_funding_opportunities.csv"'
        writer = csv.writer(response)

        writer.writerow([ 'id','name', 'provider', 'description', 'link', 'limit_per_uni',
            'external_submission_date', 'eoi_deadline','internal_submission_date','application_open_date','minimum_data_deadline','forecast_month',
            'max_amount','amount_estimated','max_duration','duration_type','duration_estimated',
            'ecr','travel','visiting_fellow','wir','phd','international','hms','ems','science','fable','is_visible'])

        FO = queryset.values_list('id','name', 'provider', 'description', 'link', 'limit_per_uni',
            'external_submission_date', 'eoi_deadline','internal_submission_date','application_open_date','minimum_data_deadline','forecast_month',
            'max_amount','amount_estimated','max_duration','duration_type','duration_estimated',
            'ecr','travel','visiting_fellow','wir','phd','international','hms','ems','science','fable','is_visible')

        #THIS FUNCTION ADDS TIME TO THE VALUES TO CONVERT FROM UTC TO PERTH/AUSTRAILIA TIME 
        def add_hours(time_string):
            the_time = datetime.datetime.strptime(time_string, '%d-%m-%Y %H:%M')
            new_time = the_time + datetime.timedelta(hours=8)
            return new_time.strftime('%d-%m-%Y %H:%M')        

        FO = [[add_hours(x.strftime("%d-%m-%Y %H:%M")) if isinstance(x, datetime.datetime) else x for x in row] for row in FO]
        
        for funding_opportunity in FO:
            writer.writerow(funding_opportunity)
        return response

    export_funding_opportunity.short_description = 'Export selected funding opportunities to csv'


    # this changes the title at /admin/fodb/funding_opportunity/
    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': 'Select Funding Opportunity to edit'}
        return super(FundingOpportunityAdmin, self).changelist_view(request, extra_context=extra_context)



    # this changes the title at /admin/fodb/funding_opportunity/6/change/
    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        response = super(FundingOpportunityAdmin, self).render_change_form(request, context, add, change, form_url, obj)
        response.context_data['title'] = "Edit Funding Opportunity" if response.context_data['object_id'] else "Add Funding Opportunity"
        return response


    def get_export_formats(self):
            """
            Returns available export formats.
            """
            formats = (
                  base_formats.CSV,
                  base_formats.XLSX,
                  base_formats.HTML,
            )
            return [f for f in formats if f().can_export()]

    

    admin.site.index_title = 'Funding Opportunities Administration'
    admin.site.site_title = 'FODB Admin'

admin.site.register(funding_opportunity,FundingOpportunityAdmin)


admin.site.unregister(Group)
