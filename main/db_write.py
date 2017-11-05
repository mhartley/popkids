# -*- coding: utf-8 -*-
from models import Person, Event
from events import eventscore
from pop_kids import settings
from django.core.management import setup_environ

import os
import sys
setup_environ(settings)

with open("test.csv","r") as f:
    line = f.readline().rstrip("\n")
    parsed = line.split("|")
    twitter_name = parsed[0]
    event_type = parsed[1]
    datetime = parsed[2]
    text = parsed[3]
    node_id = parsed[4]
    event_score = eventscore(event_type)
    score_increment = event_score
    #e = Event(event_type=event_type, score_increment=score_increment, datetime=datetime, text=text, node_id=node_id)
    #e.save()

#facebook_name = x['name']

#person_id = Person.objects.filter(twitter_name=twitter_name).count()
#b = Person(twitter_name=twitter_name, first_name=first_name, last_name=last_name, twitter_id=twitter_id)
