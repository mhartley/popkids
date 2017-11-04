from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from eventbrite import Eventbrite
import os
import requests
import json


# Create your views here.


def sendgridpost(request):
	if request.POST:
		email = request.POST.get('email')
		capture = Postdata(textdump = email)



	return HttpResponse('we got a page.')



  token = os.environ.get('EVENTBRITE_OAUTH_PERSONAL')

eventbrite = Eventbrite(token)
user = eventbrite.get_user()


def requests.get(
    "https://www.eventbriteapi.com/v3/users/me/events/",
    headers = {
        "Authorization": "Bearer 5YJ4X6TACURDGGUKRTVE",
    },
    verify = True,  # Verify SSL certificate
)

return events.json()

attendees = requests.get(
  "https://www.eventbriteapi.com/v3/users/me/owned_event_attendees/",
    headers = {
        "Authorization": "Bearer 5YJ4X6TACURDGGUKRTVE",
    },
    verify = True,  # Verify SSL certificate
  )

attendees_object = attendees.json()['attendees']

first_name = attendees_object[0]['profile']['first_name']
last_name = attendees_object[0]['profile']['last_name']
email = attendees_object[0]['profile']['email']
attendance_status = attendees_object[0]['status']


