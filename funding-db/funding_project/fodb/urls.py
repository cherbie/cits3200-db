from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='fodb-home'),
    re_path(r'^(add)|(edit)', views.db_update, name='fodb-db-update'),
    re_path(r'error', views.error, name='fodb-error'),
    re_path(r'.*', views.unknown, name='fodb-unknown') # redirects to project error page if no match
]
