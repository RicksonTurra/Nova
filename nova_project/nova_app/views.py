from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
from .models import Events
from .forms import EventForm
# from .forms import EventForm

# Create your views here.

def index(request):
    return render(request, "nova_app/index.html")

def create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("nova_app:index"))
    else:
        form = EventForm()

    return render(request, "nova_app/create.html", {
        "form": form,
    })



