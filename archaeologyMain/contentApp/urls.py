
from django.urls import path

from .views import *


urlpatterns = [
    path('dashboard', get_dashboard, name='dashboard'),
    path('buluntu/ekle', set_buluntu, name="set-buluntu")
]
