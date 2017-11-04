from django.db import models

class people(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    twitter_name = models.CharField(max_length=30)
    facebook_name = models.CharField(max_length=30)
    address = models.CharField(max_length=130)
    phone_number = models.CharField(max_length=30)
    score = models.IntegerField()

class events(models.Model):
    person_id = models.CharField(max_length=30)
    event_type = models.CharField(max_length=30)
    score_increment = models.IntegerField()
    datetime = models.DateTimeField()
    text = models.CharField(max_length=256)
    node_id = models.CharField(max_length=30)
