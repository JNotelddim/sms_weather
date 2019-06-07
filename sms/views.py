# from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from twilio.twiml.messaging_response import MessagingResponse


@csrf_exempt
def sms_response(request):
    # start our TwiML response
    resp = MessagingResponse()

    # Add a text message
    msg = resp.message("Not sure what the weather's like right now. Sorry!")

    return HttpResponse(str(resp))
