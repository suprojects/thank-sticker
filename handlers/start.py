from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CommandHandler, Filters
from html import escape
from database import botchats, botusers


def start_group(update, context):
    update.message.reply_text("I am online! 🤖", reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("OK", callback_data=(f"delete_{update.message.from_user.id}"))]]))
    botchats.update_chat(update.message.chat)

def start_pvt(update, context):
    msg, usr = update.message, update.message.from_user

    BUTTON_MARKUP = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="➕ Add me to your group ➕",url=f"http://t.me/{context.bot.username}?startgroup=start")
            ],
            [
                InlineKeyboardButton(text="Join our Channel 🔈", url="http://t.me/su_Bots"),
                InlineKeyboardButton(text="Discussion Group 💬", url="https://t.me/su_Chats"),
            ]
        ]
    )

    update.message.reply_text(text=(f"""

Hello <a href="tg://user?id={usr.id}">{escape(usr.first_name)}</a>. 👋 I am {context.bot.first_name} bot.

I will automatically send Thank you stickers to your group when it reaches 'x' members.

That is, if your group reaches 25 members, I will send the corresponding sticker. Same for all the member counts in the sticker pack.

The sticker pack I use is here 👉 <a href='https://t.me/addstickers/DownloadStics_ThankYouMembers'>Sticker Pack</a>.

Just add me to the group, and I will start working right away!

<b>P.S.: I will never see your group's messages because <a href='https://core.telegram.org/bots#privacy-mode'>Privacy mode</a> is turned on. So don't worry about spying 👀.</b>

"""), reply_markup=BUTTON_MARKUP, parse_mode='HTML', disable_web_page_preview=True)

    botusers.new_user(usr)


__handlers__ = [

    [CommandHandler("start", start_pvt, filters=Filters.chat_type.private)],
    [CommandHandler("start", start_group, filters=Filters.chat_type.groups)],
]
