from django.urls import path

from . import views

urlpatterns = [
    path('opportunity/', views.research, name='research'),
]