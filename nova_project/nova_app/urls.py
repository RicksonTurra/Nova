from django.urls import path

from . import views

app_name = "nova_app"

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("<str:eventName>", views.check, name="event"),
    path("show", views.show_events, name="show"),
    path("events", views.show_all, name="show_all"),
    path("redeem/<str:ticketIdentifier>", views.check, name="event"),
]