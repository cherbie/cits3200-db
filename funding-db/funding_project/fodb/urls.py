from django.urls import path, re_path
from .views import PostListView, PostDetailView, filter_request
from .filters import PostFilter
from .models import funding_opportunity

from . import views

urlpatterns = [
    path('', views.filter_request, name="fodb-home"),
    path('researches/', views.research, name='research'),
    # path('', PostListView.as_view(), name='fodb-home'),
    path('funding_opportunity/<int:pk>', PostDetailView.as_view(), name='funding_opportunity-detail'),
    re_path(r'^(add)|(edit)', views.db_update, name='fodb-db-update'),
    re_path(r'error', views.error, name='fodb-error'),
    re_path(r'.*', views.unknown, name='fodb-unknown') # redirects to project error page if no match
]
