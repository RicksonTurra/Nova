from .models import Events, Tickets
import json
# Get info about an specific event
def info(eventName):
    # Gets data from the database
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
    # converts data to json
    number_redeemed = json.dumps(number_redeemed)
    event_name = json.dumps(event_name)
    number_tickets = json.dumps(number_tickets)

    return event_name, number_tickets, number_redeemed