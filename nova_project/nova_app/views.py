import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core import serializers
from django import forms
from .models import Events, Tickets
from django.views.decorators.csrf import csrf_exempt
from .forms import EventForm
from . import util


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

# Render info about a specific event
def check(request, event_pk):
    # receives event info
    event_name, number_tickets, number_redeemed, event_pk = util.info(event_pk)

    # converts data from json back to python data
    number_redeemed = json.loads(number_redeemed)
    number_redeemed = int(number_redeemed)
    event_pk = json.loads(event_pk)
    number_tickets = json.loads(number_tickets)
    event_name = json.loads(event_name)


    #render page
    return render(request, "nova_app/event.html", {
        'event_name':event_name,
        'redeem': number_redeemed,
        'number': number_tickets,
        'id': event_pk
    })
#Show all events
def show_all(request):
    return render(request, "nova_app/show_all.html")

def refresh(request, id_event):
    event_name, number_tickets, number_redeemed, event_pk = util.info(id_event)

    return JsonResponse(number_redeemed, safe=False)

def ticket_status(request, tokenID):
    # get the db entry to check if it was redeemed or not
    entry = Tickets.objects.get(ticket_token = tokenID)
    status = entry.ticket_redeem
    if status == 0:
        return JsonResponse({"status": "Ticket is OK"}, status=200)
    else:
        return JsonResponse({"status": "Ticket GONE"}, status=410)

def check_status(request, IDtoken):
    return render(request, "nova_app/status.html", {
        'token': IDtoken
    })

# Redeem a ticket
def redeem(request, token):
    result = Tickets.objects.get(ticket_token = token)
    result.ticket_redeem = 1
    result.save()
    result = Tickets.objects.get(ticket_token = token)
    print(result)
    return JsonResponse({"status": "Ticket redeemed"}, status=201)

# Add tickets
@csrf_exempt
def add_ticket(request):
    data = json.loads(request.body)
    pk_event = data.get("pkid", "")
    number_tickets = int(data.get("number", ""))
    db_result = Events.objects.get(pk = pk_event)
    db_result.tickets_field = number_tickets
    db_result.save()
    event_name, number_tickets, number_redeemed, event_pk = util.info(id_event)
    print("AKIIIIIIIIIIII")
    return render(request, "nova_app/event.html", {
        'event_name':event_name,
        'redeem': number_redeemed,
        'number': number_tickets,
        'id': event_pk
    })