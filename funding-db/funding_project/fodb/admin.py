from django.contrib import admin, auth
from django.contrib.auth.models import User, Group
from .models import Post, funding_opportunity, important_date
from django.utils.html import format_html
# Register your models here.


#admin.site.register(Post)
#admin.site.register(funding_opportunity)
admin.site.register(important_date)

admin.site.site_header = 'Funding Opportunities Database'

class FundingOpportunityAdmin(admin.ModelAdmin):
	list_diplay = ['name','closing_month']
	list_filter = ('closing_month', )

admin.site.register(funding_opportunity,FundingOpportunityAdmin)


admin.site.unregister(Group)