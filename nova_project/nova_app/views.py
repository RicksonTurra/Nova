import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core import serializers
from django import forms
from .models import Events, Tickets
from .forms import EventForm


def index(request):

    return render(request, "nova_app/index.html")


def show_events(request):
    events_iterate = Events.objects.all()
    events_json = serializers.serialize('json', events_iterate)
    return JsonResponse( events_json , safe=False)

def create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()

            # Get event by name
            event_name = str(request.POST["name_field"])
            event_from_table = Events.objects.filter(name_field=event_name)

            # Get last event - required because there could be events with repeated name
            event_from_table = event_from_table.last()

            # Get id of last event
            id_event = event_from_table.id

            # Create unique token for each ticket bounded to the last event
            number_tickets = event_from_table.tickets_field
            for each in range(0, number_tickets):
                token = str(id_event) + "-" + str(each+1)
                event_token = Tickets(ticket_redeem = False, ticket_token = token, event = event_from_table)
                event_token.save()
                
            
            return HttpResponseRedirect(reverse("nova_app:index"))
    else:
        form = EventForm()
    


    return render(request, "nova_app/create.html", {
        "form": form,
    })

def check(request, ticketIdentifier):
    event = Tickets.objects.get(ticket_token = ticketIdentifier)
    event_name = event.event
    print(event_name)

    return render(request, "nova_app/event.html", {
        'event_itself':event_name
    })

def show_all(request):
    return render(request, "nova_app/show_all.html")

