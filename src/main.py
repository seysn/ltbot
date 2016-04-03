import socket
import src.config as config
from src.message import *

class Ltbot:
    def __init__(self):
        self.conf = config.get_config()
        self.sock = socket.socket()
        self.sock.settimeout(10)
        
    def connect(self):
        try:
            self.sock.connect((self.conf["host"], self.conf["port"]))
            print("[socket connected]")
            self.send(self.conf["token"], "PASS")
            self.send(self.conf["nickname"], "NICK")
            print("[received]", self.sock.recv(1024).decode("UTF-8"))
            self.send('#' + self.conf["nickname"], "JOIN")
            print("[received]", self.sock.recv(1024).decode("UTF-8"))
        except socket.error as e:
            print("[error]", "Unable to connect")
            exit(-2)
        except socket.timeout as e:
            print("[error]", "Socket timeout")
            exit(-1)

    def send(self, msg, cmd = "PRIVMSG"):
        """send a simple message"""
        SimpleMessage(msg, cmd).run(self.sock, '#' + self.conf["nickname"])

    def run(self, msg, sec, cmd = "PRIVMSG"):
        """send a message with an interval"""
        IntervalMessage(msg, cmd).run(self.sock, '#' + self.conf["nickname"], sec)
