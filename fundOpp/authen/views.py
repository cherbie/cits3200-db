from django.http import HttpResponse
from django.shortcuts import render



def login(request):
    return render(request, 'authen/login.html')