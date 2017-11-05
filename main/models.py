from django.db import models
from jsonfield import JSONField
from django.utils import timezone

class Person(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30, null=True)
	twitter_name = models.CharField(max_length=30, null=True)
	twitter_handle = models.CharField(max_length=30, null=True)
	twitter_id = models.CharField(max_length=30, null=True)
	facebook_name = models.CharField(max_length=30, null=True)
	facebook_id = models.CharField(max_length=30, null=True)
	address = models.CharField(max_length=130, null=True)
	zipcode = models.CharField(max_length=130, null=True)
	phone_number = models.CharField(max_length=30, null=True)
	email = models.EmailField(null=True)
	email2 = models.EmailField(null=True)
	score = models.IntegerField() 

class Event(models.Model):
	person = models.ForeignKey(Person)
	event_type = models.CharField(max_length=30, null=True)
	score_increment = models.IntegerField()
	datetime = models.DateTimeField()
	text = models.CharField(max_length=256, null = True)
	node_id = models.CharField(max_length=30, null = True)

class Postdata(models.Model):
	textdump = models.TextField(null = True)

class SendgridEvent(models.Model):
    kind = models.CharField(max_length=75)
    email = models.CharField(max_length=150)
    data = JSONField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
