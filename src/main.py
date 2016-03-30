import socket
import config

class Ltbot:
    def __init__(self):
        self.conf = config.get_config()
        self.sock = socket.socket()
        self.sock.settimeout(10)
        print(self.conf)
        
    def connect(self):
        self.sock.connect((self.conf["host"], self.conf["port"]))
