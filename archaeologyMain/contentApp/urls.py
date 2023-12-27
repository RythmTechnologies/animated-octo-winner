
from django.urls import path

from .views import *


urlpatterns = [
    path('dashboard', get_dashboard, name='dashboard'),
    path('buluntu/ekle', set_buluntu, name="set-buluntu"),
    path('fixture/ekle', set_fixture, name='set-fixture'),
    path('fixture/liste', fixture_list, name='fixture-liste'),
]
