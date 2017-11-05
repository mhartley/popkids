

 def eventscore(eventcode):

 	event_dictionary = {
    'fb_like':1,
    'fb_share':6,
    'fb_comment':3,
    'sg_click':1,
    'sg_open':1,
    'tw_fave':2,
    'tw_mentions':5,
    'tw_hashtags':2,
    'tw_rt':1,
    'eb_register':6,
    'eb_attendance':30,
    'ig_like':1,
    'ig_comment':3,
    'ig_save':3,
    'ig_forward':5,
    }

    if eventcode in event_dictionary.keys():
    	return event_dictionary[eventcode]
    else:
    	return 1