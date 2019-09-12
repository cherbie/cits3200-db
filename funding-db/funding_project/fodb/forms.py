from django import forms
from django_filters.widgets import BooleanWidget

class FilterForm(forms.Form):
    '''
        Note: The QuerySet generation logic has been seperated from the forms class
        This form only provides the structure requirements
    '''
    ecr = forms.BooleanField(required=False)
    travel = forms.BooleanField(required=False, initial="False")
    visiting = forms.BooleanField(required=False, initial="False")
    wir = forms.BooleanField(required=False, initial="False")
    phd = forms.BooleanField(required=False, initial="False")
    international = forms.BooleanField(required=False, initial="False")
    hms = forms.BooleanField(required=False, initial="False")
    ems = forms.BooleanField(required=False, initial="False")
    science = forms.BooleanField(required=False, initial="False")
