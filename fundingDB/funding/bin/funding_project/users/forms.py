from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

	
class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	#this form interacts with the user model because it always creates a new user
	class Meta:
		model = User
		fields = ['username','email', 'password1','password2']

#fields in the form and in the order shown
#figure out a way to only get uwa emails here 