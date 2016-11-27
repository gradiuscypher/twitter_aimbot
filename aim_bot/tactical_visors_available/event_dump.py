# This is an example Visor. Visors are meant to evaluate events and return True or False so that actions can be taken.
name = 'event_dump.py'


def activate(event_message):
    message_string = str(event_message)
    log_file = open("event_dump.log", 'a')
    log_file.write(message_string + "\n")
    print(message_string)
    log_file.close()
