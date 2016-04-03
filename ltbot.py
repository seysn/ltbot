#!/usr/bin/env python3
import src.main as ltbot

bot = ltbot.Ltbot()
bot.connect()
bot.run("hello", 15)

