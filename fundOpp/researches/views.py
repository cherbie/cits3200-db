from django.http import HttpResponse
from django.shortcuts import render



def research(request):
    return render(request, 'researches/tables.html')