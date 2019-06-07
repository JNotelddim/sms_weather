# from django.shortcuts import render
from django.http import HttpResponse


def sms_response(request):
    return HttpResponse("Hello, World.")

# Create your views here.
