from django.urls import path

from .views import *

urlpatterns = [
    path("customform", custom_form_view, name="custom-form"),
]
