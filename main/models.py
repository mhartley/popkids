from django.db import models

from django.db import models

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
	associate_id = models.CharField(max_length=100, null = True)
	score_increment = models.IntegerField()
	datetime = models.DateTimeField()
	text = models.CharField(max_length=256)
	node_id = models.CharField(max_length=30)

class Postdata(models.Model):
	textdump = models.TextField(null = True)