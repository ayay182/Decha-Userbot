from userbot import CMD_HELP, bot
from userbot.events import register


@register(outgoing=True, pattern="^.all$")
async def all(event):
    if event.fwd_from:
        return
    await event.delete()
    mentions = "@all"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, 200000):
        mentions += f"[\u2063](tg://user?id={x.id})"
    await bot.send_message(chat, mentions, reply_to=event.message.reply_to_msg_id)


CMD_HELP.update({
    "tag_all":
    "`.all`\
\nUsage: Untuk Mengetag semua anggota yang ada di group."
})
