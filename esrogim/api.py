from django.shortcuts import render
from django.http import HttpResponse
from .models import Esrog
from django.core import serializers

def json_data(request):
    esrogs = Esrog.objects.all()
    json_data = serializers.serialize('json', esrogs)
    return HttpResponse(json_data, content_type='application/json')



def data(request):
    return {
        "message": "Hello, World!"
    }