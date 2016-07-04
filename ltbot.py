#!/usr/bin/env python3
import src.main as ltbot

bot = ltbot.Ltbot()
bot.connect()
bot.send("Hello World!")
bot.loop()
