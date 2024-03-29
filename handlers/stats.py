from secrets import SUDO_USERS

from database import botchats, botusers
from telegram.ext import CommandHandler, Filters, MessageHandler
from utils import paste


def update_entities(update, context):
    botchats.update_chat(update.effective_chat)


def botuserlist(update, context):

    msg = update.message.reply_text('🔄')

    all_ = botusers.bot_users()
    res = ""

    for user in all_: res += str(user["id"]) + ' - ' + user["firstname"] + f' {user.get("lastname", "")}' + (' - @{}'.format(user['username']) if user.get('username') else '') + "\n"

    msg.edit_text(paste.neko(res))


def chatlist(update, context):

    msg = update.message.reply_text('🔄')

    all_ = botchats.all_chats()
    res = ""

    for chat in all_: res += str(chat["id"]) + ' - ' + chat["title"] + (' - {}'.format(chat['type']) if chat.get('type') else '') + (' - @{}'.format(chat['username']) if chat.get('username') else '') + "\n"

    msg.edit_text(paste.neko(res))


def stats(update, context):
    msg = update.message.reply_text('🔄')

    msg.edit_text(text = f'''
Stats of {context.bot.first_name}

👤 @{context.bot.username}
🆔 <code>{context.bot.id}</code>

🤖 Bot users: <code>{len(botusers.bot_users())}</code>
👥 Groups: <code>{len(botchats.all_chats())}</code>

''', parse_mode = 'HTML')


__handlers__ = [
    [CommandHandler("botusers", botuserlist, filters = Filters.user(SUDO_USERS), run_async=True)],
    [CommandHandler("botchats", chatlist, filters = Filters.user(SUDO_USERS), run_async=True)],
    [CommandHandler("botstats", stats, filters = Filters.user(SUDO_USERS), run_async=True)],

    [MessageHandler(Filters.all & Filters.chat_type.supergroup & ~Filters.status_update.new_chat_members & ~Filters.command, update_entities, run_async=True)],
]
