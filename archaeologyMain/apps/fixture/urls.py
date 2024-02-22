from django.urls import path

from .views import *


urlpatterns = [
    path("add", set_fixture, name="set-fixture"),
    path("list", fixture_list, name="fixture-liste"),
    path("delete/<id>", delete_fixture, name="fixture-delete"),
    path("update/<id>", update_fixture, name="fixture-update"),
    path('get-html/<id>/', get_html_content, name='get-html-content'),
]
