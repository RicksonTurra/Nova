from django.urls import path

from . import views

app_name = "nova_app"

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("event/<int:event_pk>", views.check, name="event"),
    path("show", views.show_events, name="show"),
    path("events", views.show_all, name="show_all"),
    path("event/refresh/<str:id_event>", views.refresh, name="refresh"),
    path("status/response/<str:tokenID>", views.ticket_status, name="status"),
    path("status/<str:IDtoken>", views.check_status, name="check_status"),
    path("redeem/<str:token>", views.redeem, name="redeem")
]