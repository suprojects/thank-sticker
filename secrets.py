import os

if os.path.exists('tokens.py'):

    from tokens import *
    
    os.environ['BOT_TOKEN'] = BOT_TOKEN
    os.environ['SUDO_USERS'] = '1178472788'
    os.environ['LOG_CHAT'] = LOG_CHAT


BOT_TOKEN = os.environ.get("BOT_TOKEN")
SUDO_USERS = int(os.environ.get("SUDO_USERS"))
LOG_CHAT = int(os.environ.get('LOG_CHAT'))
