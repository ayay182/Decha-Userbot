import asyncio
from userbot import CMD_HELP
from userbot.events import register

modules = CMD_HELP


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("**Maaf, Saya Tidak Punya Perintah Itu**")
            await asyncio.sleep(200)
            await event.delete()
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t✥  "
        await event.edit("**❉ Daftar Perintah Untuk Decha-Userbot ❉\n\n**"
                         f"✥{string}✥"
                         f"\n\n**Contoh** `.help afk` **Untuk Informasi Perintah AFK**")
        #await event.reply(f"\n**Contoh** `.help afk` **Untuk Informasi Perintah**")
        await asyncio.sleep(1000)
        await event.delete()
