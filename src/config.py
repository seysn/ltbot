import configparser
from os import mkdir
from os.path import expanduser, isfile, isdir

CONFIG_DIR  = expanduser("~") + "/.config/ltbot"
CONFIG_FILE = CONFIG_DIR + "/config"

def create_config():
    nickname = input("Nickname : ")
    token = input("Token : ")
    channel = input("Channel : ")
    
    config = configparser.ConfigParser()
    config["server"] = {
        "host": "irc.twitch.tv",
        "port": "6667"
    }
    config["account"] = {
        "nickname": nickname,
        "token": token,
        "channel": channel
    }

    with open(CONFIG_FILE, "w") as f:
        config.write(f)

    return config

def get_config():
    if isfile(CONFIG_FILE):
        config = configparser.ConfigParser()
        config.read(expanduser("~") + "/.config/ltbot/config")
        return config
    else:
        if input("No config file found. Do you want to generate one ? (Y/n)").upper == 'N':
            exit(0)
        else:
            if not isdir(CONFIG_DIR):
                mkdir(CONFIG_DIR)
            return create_config()
