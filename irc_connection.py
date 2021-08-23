import socket
import time


class IRC:
    irc = socket.socket()

    def __init__(self):
        # Define the socket
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, channel, msg):
        # Transfer data
        self.irc.send(bytes(f'PRIVMSG {channel} : {msg}\n', 'UTF-8'))

    def connect(self, server, port, channel, botnick, botpass):
        # Connect to the server
        print(f'Connecting to: {server}')
        self.irc.connect((server, port))

        # Perform user authentication
        self.irc.send(bytes(f'PASS {botpass}\n', 'UTF-8'))
        self.irc.send(bytes(f'NICK {botnick}\n', 'UTF-8'))
        time.sleep(1)

        # join the channel
        self.irc.send(bytes(f'JOIN {channel}\n', 'UTF-8'))

    def get_response(self):
        time.sleep(1)
        # Get the response
        resp = self.irc.recv(2040).decode('UTF-8')

        if resp.find('PING') != -1:
            self.irc.send(bytes(f"PONG {resp.split()[1]}\r\n", 'UTF-8'))

        return resp
