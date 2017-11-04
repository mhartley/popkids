from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


def sendgridpost(request):
	if request.POST:
		print(request.POST.keys())
	return HttpResponse('we got a page.')
		
