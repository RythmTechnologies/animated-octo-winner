
from django.urls import path

from .views import *


urlpatterns = [
    path('dashboard', get_dashboard, name='dashboard'),
    path('buluntu/ekle', set_buluntu, name="set-buluntu"),
    path('fixture/ekle', set_fixture, name='set-fixture'),
    path('fixture/liste', FilterListView.as_view(), name='fixture-liste'),
    path('rapor/ekle', get_rapor, name='set-rapor'),
]
