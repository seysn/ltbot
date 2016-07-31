import socket
import src.config as config
from src.message import *

class Ltbot:
    def __init__(self):
        self.conf = config.get_config()
        self.sock = socket.socket()
        self.sock.settimeout(600)

    def connect(self):
        try:
            self.sock.connect((self.conf["server"]["host"], int(self.conf["server"]["port"])))
            print("[socket connected]")
            self.send(self.conf["account"]["token"], "PASS")
            self.send(self.conf["account"]["nickname"], "NICK")
            for txt in self.sock.recv(1024).decode("UTF-8").split("\r\n")[:-1]:
                print(">", txt) 
            self.send('#' + self.conf["account"]["channel"], "JOIN")
            for txt in self.sock.recv(1024).decode("UTF-8").split("\r\n")[:-1]:
                print(">", txt)
            print()
        except socket.error as e:
            print("[error]", "Unable to connect")
            exit(-2)
        except socket.timeout as e:
            print("[error]", "Socket timeout")
            exit(-1)

    def send(self, msg, cmd = "PRIVMSG"):
        """send a simple message"""
        SimpleMessage(msg, cmd).run(self.sock, '#' + self.conf["account"]["channel"])

    def run(self, msg, sec, cmd = "PRIVMSG"):
        """send a message with an interval"""
        IntervalMessage(msg, cmd).run(self.sock, '#' + self.conf["account"]["channel"], sec)

    def loop(self):
        """main loop to analyse each message"""
        while True:
            msg = self.sock.recv(1024).decode("UTF-8")
            user = msg.split('!')[0][1:]
            
            for txt in msg.split("\r\n")[:-1]:
                print(">", txt) 
            if msg.find("PING") == 0:
                print("<", msg.replace("PING", "PONG"), end = "")
                self.sock.send(bytes(msg.replace("PING", "PONG"), "UTF-8"))
            elif msg.find("!hello") != -1:
                self.send("Hello " + user)
