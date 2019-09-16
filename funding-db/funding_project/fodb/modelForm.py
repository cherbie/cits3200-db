from django.db import models
from django.forms import ModelForm, Textarea
from .models import funding_opportunity, important_date

class funding_opportunityForm(ModelForm):
    class Meta:
        model = funding_opportunity
        fields = ['name','description','herdc', 'max_amount', 'max_duration', 'duration_type', 'amount_estimated',
        'duration_estimated', 'ecr', 'travel','visiting','wir', 'phd','international','hms','ems',
        'science','limit_per_uni', 'link', 'closing_month','is_hidden']

        widgets = {
            'description' : Textarea(attrs = {'rows' : 40, 'clos' : 60}),
        }

        help_text = {
            'description' : ('the max length is 2500.'),
            'is_hidden' : ('the opportunity will be hidden'),
            'herdc' : (''),
            'ecr' : (''),
            'travel' :(''),
            'wir' : (''),
            'phd' : (''),
            'hms' : (''),
            'ems' : (''),
            'science' : (''),

        }

        label = {
            'name' : ('opportunity name'),
            'description' : ('please describe this opportunity'),
            'max_amount' : ('the largest funding amount'),
            'max_duration' : ('the largest last time, year or month'),
            'link' : ('the link of the real funding website'),
            'closing_month' : ('Year-Month-Day H:M:S'),
        }


class important_dateForm(ModelForm):
    class Meta:
        model = important_date
        fields = ['milestone', 'date', 'date_status']

        widgets = {
            'milestone' : Textarea(attrs = {'rows' : 10, 'clos' : 20}),
        }

        help_text = {
            'milestone' : (''),
            'date_status' : (''),
        }

        label = {
            'milestone' : ('insert here'),
        }
