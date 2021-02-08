from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django import forms
from .models import Events
from .forms import EventForm
# from .forms import EventForm

# Create your views here.

def index(request):
    return render(request, "nova_app/index.html")

def create(request):
    return render(request, "nova_app/create.html", {
        "form": EventForm(),
    })


# class DateInput(forms.DateInput):
#     input_type = 'date'

# class TemplateForm(forms.Form):
#     my_date_field = forms.DateField(label="Choose Date", widget=DateInput)

