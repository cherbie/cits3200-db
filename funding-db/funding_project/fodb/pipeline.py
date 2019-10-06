# this is used to redirect users to who try to login with non uwa emails
# https://stackoverflow.com/questions/51127085/social-auth-login-error-url-not-working-django-2-0-6
from django.shortcuts import redirect

def auth_allowed(backend, details, response, *args, **kwargs):
    if not backend.auth_allowed(response, details):
        return redirect('/auth_error/')#<-here goes your url as defined on your urls.py