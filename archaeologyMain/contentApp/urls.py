
from django.urls import path

from .views import *


urlpatterns = [
    path('dashboard', get_dashboard, name='dashboard'),
]
