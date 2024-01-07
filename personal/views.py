from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def personal(request):
    template = loader.get_template("personal_app.html")
    return HttpResponse(template.render())