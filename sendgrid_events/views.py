from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from sendgrid_events.models import SendgridEvent


@require_POST
@csrf_exempt
def handle_batch_post(request):
    SendgridEvent.process_batch(data=request.raw_post_data)
    return HttpResponse()


