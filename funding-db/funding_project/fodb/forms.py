from django import forms
from django_filters.widgets import BooleanWidget

class FilterForm(forms.Form):
    '''
        Note: The QuerySet generation logic has been seperated from the forms class
        This form only provides the structure requirements
    '''
    ecr = forms.BooleanField(required=False, initial='False', label='ECR')
    travel = forms.BooleanField(required=False, initial='False', label='Travel')
    visiting = forms.BooleanField(required=False, initial='False', label='Visiting')
    wir = forms.BooleanField(required=False, initial='False', label='Women in Research')
    phd = forms.BooleanField(required=False, initial='False', label='PhD')
    international = forms.BooleanField(required=False, initial='False', label='International')
    hms = forms.BooleanField(required=False, initial='False', label='HMS')
    ems = forms.BooleanField(required=False, initial='False', label='EMS')
    science = forms.BooleanField(required=False, initial='False', label='Science')
