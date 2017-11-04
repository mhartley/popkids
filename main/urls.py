from django.conf.urls import url
from . import views


urlpatterns = [
    # url(r'^hello/', views.helloworld),
    url(r'sendgridpost', views.sendgridpost)
]
