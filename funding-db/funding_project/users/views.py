from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# Auth test 2
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

# Create your views here.
#if it is just a post request then just display then check if it is valid and display the name

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your Funding Opportunities account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            #return HttpResponse('Please confirm your email address to complete the registration')
            return render(request, 'users/auth_confirm.html')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request,'users/profile.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        return render(request, 'users/auth_complete.html')
    else:
        # return HttpResponse('Activation link is invalid!')
        return render(request, 'users/auth_invalid.html')


def auth_error(request):
	'''
		Redirects to auth error page.
	'''
	return render(request, 'users/auth_error.html')