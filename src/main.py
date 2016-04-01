import socket
import src.config as config

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
        print("[send]", cmd, msg)
        if cmd == "PRIVMSG":
            self.sock.send(bytes("PRIVMSG %s :%s\r\n" % ('#' + self.conf["nickname"], msg), "UTF-8"))
        else:
            self.sock.send(bytes("%s %s\r\n" % (cmd, msg), "UTF-8"))
