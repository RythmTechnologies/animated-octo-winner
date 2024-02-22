from django.urls import path

from .views import *

urlpatterns = [
    path("add", add_rapor, name="create-rapor"),
    path("list", get_rapor_list, name="rapor-liste"),
    path("delete/<id>", delete_rapor, name="delete-rapor"),
    path("update/<id>", update_rapor, name="update-rapor"),
    path('get-html/<id>/', get_html_content, name='get-html-content'),
]
