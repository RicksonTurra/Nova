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
    # Endpoint to check the status of a ticket - returns a JSON.
    path("status/response/<str:tokenID>", views.ticket_status, name="status"),
    # Endpoint that renders a ticket status
    path("status/<str:IDtoken>", views.check_status, name="check_status"),
    path("redeem/<str:token>", views.redeem, name="redeem"),
    path("add", views.add_ticket, name="add")
]