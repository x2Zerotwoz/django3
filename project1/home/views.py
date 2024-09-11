from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())


def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())