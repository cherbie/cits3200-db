from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.opportunities, name='fodb-home'),
    # path('about', views.about, name='fodb-about'),
    re_path(r'error', views.error, name='fodb-error'),
    re_path(r'.*', views.unknown, name='fodb-unknown') # redirects to project error page if no match
]
