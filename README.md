# Nova

Nova project.

It creates a system that implements the creation of a rudimentary event ticket management.
The overall goal is to be able to create events and manage the number of people accessing each event.

The application has a web page to create events - which is implemented by the route "/create".
In order to create an event, type the name of the event, the number of tickets and choose a date for the particular event.

The app has only one user - therefore it was added no authentication service.

There is a page to check all of the events - which can be reached through the button "Show Events" on the index page or through the route "/events".

The route to check an specific event is ```/event/<str:EventID>``` ==> something like "/event/2".
From the page of a specific event, the user should be able to see the total number of tickets, how many tickets have been redeemed and a button to refresh the counters.
From this page, it is also possible to add more tickets to this particular event.

Each ticket is represented by a unique token - and has the following format "{"event_id"+"-"+"number"} ==> something like {3-1} for the event 3 with identification 1; so, ticket "3-1".

The system has a page to check the status of a specific ticket - which is reached through the route ```/status/<str:ticket_token>``` ==> something like "/status/2-4".
From this page, the user is going to have acces to whether a ticket has been redeemed or not - in case it has, it is going to render the message "Ticket GONE"; in case it has not, it is going to render the message "Ticket OK". And, last case scenario, if the does not exist, the message "Ticket does not exist" is going to be rendered.
In case the ticket has not been redeemed, there is going to be a button allowing the user to redeem such ticket.

The endpoint to redeem a ticket is ```redeem/<str:token>```.

The system was created using Django and SQLite database - the reason why I have used SQLite database is that this app is supposed to contain only one user and Django has the ability to build the database itself.

It has been dockerised.

In order to run the app, run ```docker-compose up``` from the Nova folder.  









