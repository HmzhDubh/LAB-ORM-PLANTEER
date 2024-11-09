from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import Contact
from plantApp.models import Plant
from .forms import ContactForm
# Create your views here.


def home_view(request: HttpRequest):

    plants = Plant.objects.all()[0:3]
    return render(request, 'index.html', context={'plants': plants})


def contact_view(request: HttpRequest):

    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('main:contact_messages_view')
            # print(request.POST)
        else: print("Form is Not Valid")


    request = render(request, 'contact.html')
    return request


def contact_messages_view(request: HttpRequest):
    msgs = Contact.objects.all()
    return render(request, 'contact_messages.html', context={'msgs': msgs})

