from threading import (Thread, Timer)
import time

class SimpleMessage(Thread):
    # TODO Add other commands
    list_cmd = ["PASS", "NICK", "JOIN", "PRIVMSG"]

    def __init__(self, msg, cmd = "PRIVMSG"):
        if cmd not in self.list_cmd:
            raise Exception("Command is not correct or not implemented")
        Thread.__init__(self)
        self.cmd = cmd
        self.msg = msg

    def run(self, socket, chan = None, sec = 0):
        time.sleep(sec)
        print("<", self.cmd, self.msg)
        if self.cmd == "PRIVMSG":
            if chan is None:
                raise Exception("There must be a channel when sending PRIVMSG")
            else:
                socket.send(bytes("PRIVMSG %s :%s\r\n" % (chan, self.msg), "UTF-8"))
        else:
            socket.send(bytes("%s %s\r\n" % (self.cmd, self.msg), "UTF-8"))

class IntervalMessage(Thread):
    def __init__(self, msg, cmd = "PRIVMSG"):
        self.message = SimpleMessage(msg, cmd)

    def run(self, socket, chan, sec):
        def func_wrapper():
            self.message.run(socket, chan)
            self.run(socket, chan, sec)
        t = Timer(sec, func_wrapper)
        t.start()
        return t
