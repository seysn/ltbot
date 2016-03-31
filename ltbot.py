#!/usr/bin/env python3
import src.main as ltbot
import threading

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

def send_hello():
    bot.send("Hello world")

bot = ltbot.Ltbot()
bot.connect()
set_interval(send_hello, 15)

