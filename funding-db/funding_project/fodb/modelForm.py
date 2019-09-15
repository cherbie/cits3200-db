from django.db import models
from django.forms import ModelForm

class funding_opportunityForm(ModelForm):
    class Meta:
        model = funding_opportunity
        fields = ['name','description','herdc', 'max_amount', 'max_duration', 'duration_type' 'amount_estimated',
        'duration_estimated', 'ecr', 'travel','visiting','wir', 'phd','international','hms','ems,
        'science','limit_per_uni', 'link', 'closing_month','creation_date','last_updated','is_hidden']

        widgets = {
            'description' = forms.TextInput(attrs = {'size' : '200'})
        }


class important_dateForm(ModelForm):
    class Meta:
        model = important_date
        fields = ['milestone', 'date', 'date_status']
