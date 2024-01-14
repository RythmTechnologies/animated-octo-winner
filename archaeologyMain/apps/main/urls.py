from django.urls import path

from .views import *

urlpatterns = [
  path('main', get_dashboard, name="dashboard")
]

