from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.


def home_view(request: HttpRequest):

    return render(request, 'index.html')


def contact_view(request: HttpRequest):
    return render(request, 'contact.html')


def contact_messages_view(request: HttpRequest):
    return render(request, 'contact_messages.html')
