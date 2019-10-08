from django import forms
from django_filters.widgets import BooleanWidget
from django.forms import ModelForm, Textarea
from .models import funding_opportunity

class FilterForm(forms.Form):
    '''
        Note: The QuerySet generation logic has been seperated from the forms class
        This form only provides the structure requirements
    '''
    sorting = [
        ('asc', 'A-Z'),
        ('desc', 'Z-A'),
        ('close-asc', 'Closest deadline'),
        ('close-desc', 'Furthest deadline')]
    sort = forms.ChoiceField(required=False, initial='asc', choices=sorting, label='Sort by')
    ecr = forms.BooleanField(required=False, initial='False', label='ECR')
    travel = forms.BooleanField(required=False, initial='False', label='Travel')
    visiting = forms.BooleanField(required=False, initial='False', label='Visiting')
    wir = forms.BooleanField(required=False, initial='False', label='Women in Research')
    phd = forms.BooleanField(required=False, initial='False', label='PhD')
    international = forms.BooleanField(required=False, initial='False', label='International')
    hms = forms.BooleanField(required=False, initial='False', label='HMS')
    ems = forms.BooleanField(required=False, initial='False', label='EMS')
    science = forms.BooleanField(required=False, initial='False', label='Science')
    fable = forms.BooleanField(required=False, initial='False', label='FABLE')

class funding_opportunityForm(ModelForm):
    class Meta:
        model = funding_opportunity
        fields = ['name','description', 'max_amount', 'max_duration', 'duration_type', 'amount_estimated',
        'duration_estimated', 'ecr', 'travel','visiting','wir', 'phd','international','hms','ems',
        'science','limit_per_uni', 'link', 'closing_date','is_hidden']


        help_text = {
            'description' : ('the max length is 2500.'),
            'is_hidden' : ('the opportunity will be hidden')
        }

        label = {
            'name' : ('opportunity name'),
            'description' : ('please describe this opportunity'),
            'max_amount' : ('the largest funding amount'),
            'max_duration' : ('the largest last time, year or month'),
            'link' : ('the link of the real funding website'),
            'closing_date' : ('Year-Month-Day H:M:S'),
        }


