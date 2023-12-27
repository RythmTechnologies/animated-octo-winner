import django_filters
from .models import Fixture

class FixtureFilter(django_filters.FilterSet):


    class Meta:
        model = Fixture
        fields = ['name', 'marka', 'model', 'piece', 'custodian',]
    