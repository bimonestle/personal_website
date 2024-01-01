from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def calc_avg_sess(request):
    # return HttpResponse("Hello, This is Calculate Average Sessions project!") # testing only
    template = loader.get_template("my_first.html")
    return HttpResponse(template.render())