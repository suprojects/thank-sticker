from utils.pack import pack
from telegram.ext import MessageHandler, Filters


def join(update, context):

    memberCount = context.bot.get_chat_members_count(update.message.chat_id)
    StickerID = pack.get(memberCount)

    if (StickerID != None):

        try:
            update.message.reply_sticker(sticker=StickerID, quote=False)

        except:
            update.message.reply_text(text=(f"<b>THANK YOU FOR {memberCount} MEMBERS</b>"), parse_mode='HTML', quote=False)


__handlers__ = [
    [MessageHandler(Filters.status_update.new_chat_members, join)]
]
