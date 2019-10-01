from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    def clean_email(self):
        data = self.cleaned_data['email']
        if "@student.uwa.edu.au" not in data:   # any check you need
            raise forms.ValidationError("Must be a uwa student address")
        return data


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
