# from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# from django.shortcuts import render

from twilio.twiml.messaging_response import MessagingResponse
import requests


@csrf_exempt
def sms_response(request):
    # start our TwiML response
    resp = MessagingResponse()

    # Add a text message
    resp.message("Not sure what the weather's like right now. Sorry!")

    return HttpResponse(str(resp))


@csrf_exempt
def get_weather(request):
    APP_KEY = '9fcefe16638b30d1720add7e6e11280a'
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=victoria&units=metric&appid='+APP_KEY)
    return HttpResponse(response)
