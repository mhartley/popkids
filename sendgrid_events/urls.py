

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r"^batch/$", views.handle_batch_post, name="sendgrid_handle_batch_post")
]
