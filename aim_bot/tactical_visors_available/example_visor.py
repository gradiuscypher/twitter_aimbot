from pprint import pprint


name = 'example_visor.py'
"""
{'created_at': 'Sat Jun 25 06:22:47 +0000 2016',
 'event': 'favorite',
 'source': {'contributors_enabled': False,
            'created_at': 'Sat Nov 03 01:02:37 +0000 2012',
            'default_profile': False,
            'default_profile_image': False,
            'description': 'Infosec dude at Riot Games. My tweets are my own. '
                           'https://discord.gg/0Z1B5SVKFke6q17z',
            'favourites_count': 8944,
            'follow_request_sent': None,
            'followers_count': 7050,
            'following': None,
            'friends_count': 1095,
            'geo_enabled': False,
            'id': 922149583,
            'id_str': '922149583',
            'is_translation_enabled': False,
            'is_translator': False,
            'lang': 'en',
            'listed_count': 80,
            'location': 'on an internet spaceship',
            'name': 'RiotGradius',
            'notifications': None,
            'profile_background_color': '131516',
            'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme14/bg.gif',
            'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme14/bg.gif',
            'profile_background_tile': True,
            'profile_banner_url': 'https://pbs.twimg.com/profile_banners/922149583/1456535832',
            'profile_image_url': 'http://pbs.twimg.com/profile_images/706015572442546176/qVNK6otS_normal.jpg',
            'profile_image_url_https': 'https://pbs.twimg.com/profile_images/706015572442546176/qVNK6otS_normal.jpg',
            'profile_link_color': '222B2B',
            'profile_sidebar_border_color': 'FFFFFF',
            'profile_sidebar_fill_color': 'EFEFEF',
            'profile_text_color': '333333',
            'profile_use_background_image': True,
            'protected': False,
            'screen_name': 'RiotGradius',
            'statuses_count': 16090,
            'time_zone': None,
            'url': 'http://www.grds.io',
            'utc_offset': None,
            'verified': False},
 'target': {'contributors_enabled': False,
            'created_at': 'Sat Nov 03 01:02:37 +0000 2012',
            'default_profile': False,
            'default_profile_image': False,
            'description': 'Infosec dude at Riot Games. My tweets are my own. '
                           'https://discord.gg/0Z1B5SVKFke6q17z',
            'favourites_count': 8944,
            'follow_request_sent': None,
            'followers_count': 7050,
            'following': None,
            'friends_count': 1095,
            'geo_enabled': False,
            'id': 922149583,
            'id_str': '922149583',
            'is_translation_enabled': False,
            'is_translator': False,
            'lang': 'en',
            'listed_count': 80,
            'location': 'on an internet spaceship',
            'name': 'RiotGradius',
            'notifications': None,
            'profile_background_color': '131516',
            'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme14/bg.gif',
            'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme14/bg.gif',
            'profile_background_tile': True,
            'profile_banner_url': 'https://pbs.twimg.com/profile_banners/922149583/1456535832',
            'profile_image_url': 'http://pbs.twimg.com/profile_images/706015572442546176/qVNK6otS_normal.jpg',
            'profile_image_url_https': 'https://pbs.twimg.com/profile_images/706015572442546176/qVNK6otS_normal.jpg',
            'profile_link_color': '222B2B',
            'profile_sidebar_border_color': 'FFFFFF',
            'profile_sidebar_fill_color': 'EFEFEF',
            'profile_text_color': '333333',
            'profile_use_background_image': True,
            'protected': False,
            'screen_name': 'RiotGradius',
            'statuses_count': 16090,
            'time_zone': None,
            'url': 'http://www.grds.io',
            'utc_offset': None,
            'verified': False},
 'target_object': {'contributors': None,
                   'coordinates': None,
                   'created_at': 'Sat Jun 25 05:44:53 +0000 2016',
                   'entities': {'hashtags': [],
                                'symbols': [],
                                'urls': [],
                                'user_mentions': []},
                   'favorite_count': 26,
                   'favorited': False,
                   'geo': None,
                   'id': 746579899876466689,
                   'id_str': '746579899876466689',
                   'in_reply_to_screen_name': None,
                   'in_reply_to_status_id': None,
                   'in_reply_to_status_id_str': None,
                   'in_reply_to_user_id': None,
                   'in_reply_to_user_id_str': None,
                   'is_quote_status': False,
                   'lang': 'en',
                   'place': None,
                   'retweet_count': 1,
                   'retweeted': False,
                   'source': '<a href="http://twitter.com" '
                             'rel="nofollow">Twitter Web Client</a>',
                   'text': 'Could you guys do me an awesome favor and favorite '
                           "this tweet? I'm working on my anti-bot script and "
                           'need to confirm something. :)',
                   'truncated': False,
                   'user': {'contributors_enabled': False,
                            'created_at': 'Sat Nov 03 01:02:37 +0000 2012',
                            'default_profile': False,
                            'default_profile_image': False,
                            'description': 'Infosec dude at Riot Games. My '
                                           'tweets are my own. '
                                           'https://discord.gg/0Z1B5SVKFke6q17z',
                            'favourites_count': 8944,
                            'follow_request_sent': None,
                            'followers_count': 7050,
                            'following': None,
                            'friends_count': 1095,
                            'geo_enabled': False,
                            'id': 922149583,
                            'id_str': '922149583',
                            'is_translation_enabled': False,
                            'is_translator': False,
                            'lang': 'en',
                            'listed_count': 80,
                            'location': 'on an internet spaceship',
                            'name': 'RiotGradius',
                            'notifications': None,
                            'profile_background_color': '131516',
                            'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme14/bg.gif',
                            'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme14/bg.gif',
                            'profile_background_tile': True,
                            'profile_banner_url': 'https://pbs.twimg.com/profile_banners/922149583/1456535832',
                            'profile_image_url': 'http://pbs.twimg.com/profile_images/706015572442546176/qVNK6otS_normal.jpg',
                            'profile_image_url_https': 'https://pbs.twimg.com/profile_images/706015572442546176/qVNK6otS_normal.jpg',
                            'profile_link_color': '222B2B',
                            'profile_sidebar_border_color': 'FFFFFF',
                            'profile_sidebar_fill_color': 'EFEFEF',
                            'profile_text_color': '333333',
                            'profile_use_background_image': True,
                            'protected': False,
                            'screen_name': 'RiotGradius',
                            'statuses_count': 16090,
                            'time_zone': None,
                            'url': 'http://www.grds.io',
                            'utc_offset': None,
                            'verified': False}}}
"""


def activate(event_message, config, twitter):
    if "user" in event_message.keys():
        print("UserEvent")
        pprint(event_message)

    if "event" in event_message.keys():
        print("EventEvent")
        pprint(event_message)

    if "entities" in event_message.keys():
        print("EntitiesEvent")
        pprint(event_message['entities'])
        pprint(event_message['entities'].keys())
        if "urls" in event_message['entities'].keys():
            print("URLEvent")
            # pprint(event_message['entities']['urls'])
            for url in event_message['entities']['urls']:
                pprint(url['expanded_url'])

    else:
        print("NotEstablishedEvent")
        pprint(event_message)
