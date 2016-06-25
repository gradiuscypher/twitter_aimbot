# This is an example Visor. Visors are meant to evaluate events and return True or False so that actions can be taken.
name = 'example_visor.py'


def activate(event_message):
    event_type = event_message['event']
    source = event_message['source']['name']
    followers = event_message['source']['followers_count']
    bio = event_message['source']['description']
    print("Event type: {} | Source: {} | Followers: {} | Bio: {}".format(event_type, source, followers, bio))
    return True
