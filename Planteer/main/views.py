from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import Contact
from plantApp.models import Plant
# Create your views here.


def home_view(request: HttpRequest):

    plants = Plant.objects.all()
    return render(request, 'index.html', context={'plants': plants})


def contact_view(request: HttpRequest):

    if request.method == "POST":
        new_msg = Contact(

            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            message=request.POST['message'],

        )

        new_msg.save()
        print(request.POST)
        request = redirect('main:contact_messages_view')
        return request

    request = render(request, 'contact.html')
    return request


def contact_messages_view(request: HttpRequest):
    msgs = Contact.objects.all()
    return render(request, 'contact_messages.html', context={'msgs': msgs})

