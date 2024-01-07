from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def personal(request):
    template = loader.get_template("personal_app.html")
    return HttpResponse(template.render())

def calculate_avg_sessions(request):
    template = loader.get_template("calc_avg_sess.html")
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template("testing.html")
    context = {
        "fruits": ["Apple", "Banana", "Cherry"],
    }
    return HttpResponse(template.render(context, request))