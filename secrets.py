try:
    from config import *

except ImportError:
    pass

import os   

BOT_TOKEN = os.environ.get("BOT_TOKEN")
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS").split()))
LOG_CHAT = int(os.environ.get('LOG_CHAT'))
