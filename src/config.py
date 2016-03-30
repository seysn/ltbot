from os.path import expanduser

def get_config():
    config = {}
    config["host"] = "irc.twitch.tv"
    config["port"] = 6667
    config["nickname"], config["token"] = get_account()
    return config

def get_account():
    with open(expanduser("~") + "/.config/ltbot.conf") as f:
        nick = f.readline().replace('\n', '')
        token = f.readline().replace('\n', '')
    return (nick, token)
