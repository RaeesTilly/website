from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def bandapp(request):
    template = loader.get_template('theband.html')
    return HttpResponse(template.render())
