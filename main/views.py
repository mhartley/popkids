from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


def sendgridpost(request):
	if request.POST:
		email = request.POST.get('email')
		capture = Postdata(textdump = email)



	return HttpResponse('we got a page.')
		
