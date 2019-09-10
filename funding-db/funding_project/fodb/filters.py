from .models import funding_opportunity
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = funding_opportunity
        fields = ['ecr', 'travel', 'visiting', 'wir', 'phd', 'international', 'hms', 'ems', 'science']
        
