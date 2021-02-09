from django.urls import path

from . import views

app_name = "nova_app"

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("redeem/<str:ticketIdentifier>", views.check, name="event")
]