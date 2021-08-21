from irc import *
import json


# IRC Config
server = 'irc.chat.twitch.tv'
port = 6667
channel = "#"
botnick = ""
botpass = json.load(open('secrets.json'))['chatbot_pass']


def chat():
    while True:
        text = irc.get_response()
        print(text)

        if 'PRIVMSG' in text and channel in text and 'hello' in text.lower():
            irc.send(channel, 'Hello!')


if __name__ == "__main__":
    # connection to Twitch chat
    irc = IRC()
    irc.connect(server, port, channel, botnick, botpass)

    chat()
