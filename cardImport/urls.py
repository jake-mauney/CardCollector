from django.urls import path

from . import views

urlpatterns = [
    path("", views.importpage, name="import"),
]