from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='fodb-home'),
    path('about/', views.about, name='fodb-about'),
   
]

