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

def check(request, eventName):
    event = Events.objects.get(name_field = eventName)
    event_name = event.name_field
    number_tickets = event.tickets_field
    number_redeemed = 0
    # Calculate the amount of tickets redemeed
    for number in range (1, number_tickets+1):
        # Define variable with the value of a token
        token = f"{event.id}-{number}"
        ticket = Tickets.objects.get(ticket_token = token)
        redeem = ticket.ticket_redeem
        # If ticket was redeemed add one more to the count of tickets redemeed
        if redeem == True:
            number_redeemed += 1

    
    print(event)

    return render(request, "nova_app/event.html", {
        'event_name':event_name,
        'redeem': number_redeemed,
        'number': number_tickets,

    })

def show_all(request):
    return render(request, "nova_app/show_all.html")

