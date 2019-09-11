import django_filters
from django.db import models
from .models import funding_opportunity
from .forms import FilterForm
from django_filters.widgets import BooleanWidget
from django.db.models import Q

class PostFilter(django_filters.FilterSet):
    ecr = django_filters.BooleanFilter(field_name="ecr", label="ECR", distinct=True, widget=BooleanWidget())
    travel = django_filters.BooleanFilter(field_name="travel", label="Travel", distinct=True, widget=BooleanWidget())
    visiting = django_filters.BooleanFilter(field_name="visiting", label="Visiting", distinct=True, widget=BooleanWidget())
    wir = django_filters.BooleanFilter(field_name="wir", label="Women in Research", distinct=True, widget=BooleanWidget())
    phd = django_filters.BooleanFilter(field_name="phd", label="PhD",distinct=True, widget=BooleanWidget())
    international = django_filters.BooleanFilter(field_name="international", label="International", distinct=True, widget=BooleanWidget())
    hms = django_filters.BooleanFilter(field_name="hms", label="HMS", distinct=True, widget=BooleanWidget(), exclude=True)
    ems = django_filters.BooleanFilter(field_name="ems", label="EMS", distinct=True, widget=BooleanWidget(), exclude=True)
    science = django_filters.BooleanFilter(field_name="science", label="Science", distinct=True, widget=BooleanWidget(), exclude=True)


    class Meta:
        model = funding_opportunity
        fields = ['ecr', 'travel', 'visiting', 'wir', 'phd', 'international', 'hms', 'ems', 'science']
        # form = FilterForm

class FilterManager(models.Manager):
    """
        Customly manage filters.
    """
    fields = {
        'hms': Q(hms="True"),
        'ems': Q(ems="True"),
        'science': Q(science="True"),
        'travel': Q(travel="True"),
        'ecr': Q(ecr=True),
        'international': Q(international=True),
        'wir': Q(wir=True),
        'phd': Q(phd=True),
        'visiting': Q(visiting=True),

    }
    static filter(dict):
        qs = super().get_queryset()
        if len(dict) == 0:
            return qs
        else:
            count = True
            res = qs
            for key in dict:
                if count:
                    res.intersection(qs.filter(self.fields[key]))
                    count = False
                else:
                    res.union(qs.filter(self.fields[key]))
            return res
