import twitter
import configparser
from os import listdir
from importlib import import_module


class Aimbot:

    def __init__(self, config_file):
        config = configparser.RawConfigParser()
        config.read(config_file)
        consumer_key = config.get("Twitter", "consumer_key")
        consumer_secret = config.get("Twitter", "consumer_secret")
        access_token = config.get("Twitter", "access_token")
        access_secret = config.get("Twitter", "access_secret")
        self.debug = config.getboolean("Settings", "debug")
        self.auth = twitter.OAuth(consumer_key=consumer_key, consumer_secret=consumer_secret, token=access_token,
                                  token_secret=access_secret)
        self.loaded_visors = []
        self.visor_dir = 'tactical_visors_active'

    def load_visors(self):
        visor_count = 0

        for file_name in listdir(self.visor_dir):
            if not file_name.startswith('_') and file_name.endswith('.py'):
                module_name = file_name.replace('.py', '')
                self.loaded_visors.append(import_module(self.visor_dir + '.' + module_name))
                print("Tactical Visor Activated: [{}]".format(file_name))
                visor_count += 1
        print("You have {} Tactical Visors activated.".format(visor_count))

    def evaluate_target(self, event_message):
        for visor in self.loaded_visors:
            if visor.activate(event_message):
                # print("{} came back true!".format(visor.name))
                pass

    def visor_loop(self):
        self.load_visors()

        stream = twitter.stream.TwitterStream(auth=self.auth, domain='userstream.twitter.com')

        for message in stream.user():
            if 'event' in message:
                self.evaluate_target(message)
            if self.debug:
                message_string = str(message)
                log_file = open("event_dump.log", 'a')
                log_file.write(message_string + "\n")
                print(message_string)
                log_file.close()
