from django import forms
from django_filters.widgets import BooleanWidget

class FilterForm(forms.Form):
    ecr = forms.BooleanField(required=False, initial="True")
    travel = forms.BooleanField(required=False, initial="True")
    visiting = forms.BooleanField(required=False, initial="True")
    wir = forms.BooleanField(required=False, initial="True")
    phd = forms.BooleanField(required=False, initial="True")
    international = forms.BooleanField(required=False, initial="True")
    hms = forms.BooleanField(required=False, initial="True")
    ems = forms.BooleanField(required=False, initial="True")
    science = forms.BooleanField(required=False, initial="True")
