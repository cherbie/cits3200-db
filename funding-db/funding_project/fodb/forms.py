from django import forms
from django_filters.widgets import BooleanWidget
from django.forms import Textarea
from .models import funding_opportunity

class FilterForm(forms.Form):
    '''
        Note: The QuerySet generation logic has been seperated from the forms class
        This form only provides the structure requirements
    '''
    sorting = [
        ('asc', 'A-Z'),
        ('desc', 'Z-A'),
        ('close-asc', 'Nearest deadline'),
        ('close-desc', 'Furthest deadline')
    ]
    months = [
        ('-1', 'N/A'),
        ('1', 'JAN'),
        ('2', 'FEB'),
        ('3', 'MAR'),
        ('4', 'APR'),
        ('5', 'MAY'),
        ('6', 'JUN'),
        ('7', 'JUL'),
        ('8', 'AUG'),
        ('9', 'SEP'),
        ('10', 'OCT'),
        ('11', 'NOV'),
        ('12', 'DEC')
    ]
    sort = forms.ChoiceField(required=False, initial='close-asc', choices=sorting, label='Sort by')
    ecr = forms.BooleanField(required=False, initial='False', label='ECR')
    travel = forms.BooleanField(required=False, initial='False', label='Travel')
    visiting = forms.BooleanField(required=False, initial='False', label='Visiting Fellow')
    wir = forms.BooleanField(required=False, initial='False', label='Women in Research')
    phd = forms.BooleanField(required=False, initial='False', label='PhD')
    international = forms.BooleanField(required=False, initial='False', label='International')
    hms = forms.BooleanField(required=False, initial='False', label='HMS')
    ems = forms.BooleanField(required=False, initial='False', label='EMS')
    science = forms.BooleanField(required=False, initial='False', label='Science')
    fable = forms.BooleanField(required=False, initial='False', label='FABLE')
    month = forms.ChoiceField(required=False, initial='-1', choices=months, label='Month')
    search = forms.CharField(required=False, initial="", max_length=200, strip=False)


class NewAdminForm(forms.ModelForm):
    class Media:
        js = ("/static/fodb/js/base2.js",
            "/static/fodb/js/jquery-3.4.1.min.js"
        )
    def clean(self):
        max_duration = self.cleaned_data.get('max_duration')
        duration_type = self.cleaned_data.get('duration_type')
        
        if max_duration is not None and duration_type is None:
            msg = forms.ValidationError("This field is required.")
            self.add_error('duration_type', msg)
        elif duration_type is not None and max_duration is None:
            msg = forms.ValidationError("This field is required.")
            self.add_error('max_duration', msg)
        '''
        else:
            # Keep the database consistent. The user may have
            # submitted a duration_type even if max_duration
            # was not selected
            self.cleaned_data['duration_type'] = ''
            '''

        return self.cleaned_data