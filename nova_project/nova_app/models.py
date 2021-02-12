from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator
# Create your models here.
class Events(models.Model):
    name_field = models.CharField(max_length=200)
    tickets_field = models.IntegerField(validators = [MinValueValidator(limit_value=0)])
    date_field = models.DateField()

    def __str__(self):
        return f"{self.name_field} {self.tickets_field} {self.date_field}"

class Tickets(models.Model):
    ticket_redeem = models.BooleanField(default=False)
    ticket_token = models.CharField(max_length=200)
    event = models.ForeignKey(Events, on_delete=models.CASCADE, default = None, null = True, blank = True)

    def __str__(self):
        return f"redeemed: {self.ticket_redeem} Token: {self.ticket_token}"
