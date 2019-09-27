from django.db import models
from django.forms import ModelForm, Textarea
from .models import funding_opportunity

class funding_opportunityForm(ModelForm):
    class Meta:
        model = funding_opportunity
        fields = ['name','description', 'max_amount', 'max_duration', 'duration_type', 'amount_estimated',
        'duration_estimated', 'ecr', 'travel','visiting','wir', 'phd','international','hms','ems',
        'science','limit_per_uni', 'link', 'closing_month','is_hidden']

        widgets = {
            'description' : Textarea(attrs = {'rows' : 40, 'clos' : 60}),
        }

        help_text = {
            'description' : ('the max length is 2500.'),
            'is_hidden' : ('the opportunity will be hidden'),

        }

        label = {
            'name' : ('opportunity name'),
            'description' : ('please describe this opportunity'),
            'max_amount' : ('the largest funding amount'),
            'max_duration' : ('the largest last time, year or month'),
            'link' : ('the link of the real funding website'),
            'closing_month' : ('Year-Month-Day H:M:S'),
        }

