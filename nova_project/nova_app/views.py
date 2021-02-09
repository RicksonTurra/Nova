from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
from .models import Events, Tickets
from .forms import EventForm


def index(request):
    return render(request, "nova_app/index.html")

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

            # Create unique token (id) for each ticket bounded to the last event
            number_tickets = event_from_table.tickets_field
            for each in range(0, number_tickets):
                event_token = Tickets(ticket_redeem = False, ticket_token = each+1, event = event_from_table)
                event_token.save()
                last_ticket = Tickets.objects.all().last().ticket_token
                print(last_ticket)
            
            return HttpResponseRedirect(reverse("nova_app:index"))
    else:
        form = EventForm()
    


    return render(request, "nova_app/create.html", {
        "form": form,
    })



