from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Events(models.Model):
    name_field = models.CharField(max_length=200)
    tickets_field = models.IntegerField()
    date_field = models.DateField()

class Tickets(models.Model):
    ticket_token = models.BooleanField(default=False)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)