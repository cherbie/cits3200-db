from django.shortcuts import render
from django.http import HttpResponse

def welcome_page(request):
    return HttpResponse('Welcome to the funding opportunities database.');