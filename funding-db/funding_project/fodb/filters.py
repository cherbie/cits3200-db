from .models import funding_opportunity
import django_filters
from .forms import FilterForm
from django_filters.widgets import BooleanWidget


class PostFilter(django_filters.FilterSet):
    ecr = django_filters.BooleanFilter(field_name="ecr", label="ECR", distinct=True, widget=BooleanWidget())
    travel = django_filters.BooleanFilter(field_name="travel", label="Travel", distinct=True, widget=BooleanWidget())
    visiting = django_filters.BooleanFilter(field_name="visiting", label="Visiting", distinct=True, widget=BooleanWidget())
    wir = django_filters.BooleanFilter(field_name="wir", label="Women in Research", distinct=True, widget=BooleanWidget())
    phd = django_filters.BooleanFilter(field_name="phd", label="PhD",distinct=True, widget=BooleanWidget())
    international = django_filters.BooleanFilter(field_name="international", label="International", distinct=True, widget=BooleanWidget())
    hms = django_filters.BooleanFilter(field_name="hms", label="HMS", distinct=True, widget=BooleanWidget())
    ems = django_filters.BooleanFilter(field_name="ems", label="EMS", distinct=True, widget=BooleanWidget())
    science = django_filters.BooleanFilter(field_name="science", label="Science", distinct=True, widget=BooleanWidget())


    class Meta:
        model = funding_opportunity
        fields = ['ecr', 'travel', 'visiting', 'wir', 'phd', 'international', 'hms', 'ems', 'science']
        form = FilterForm
