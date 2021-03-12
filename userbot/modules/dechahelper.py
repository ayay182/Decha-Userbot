
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.dechahelp$")
async def usit(e):
    await e.edit(
        f"Hai {DEFAULTUSER} Kalo Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Telegram](t.me/ayay182)"
        "\n[Repo](https://github.com/ayay182/Decha-Userbot)")


@register(outgoing=True, pattern="^.dechavar$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/ayay182/Decha-Userbot/Decha-Userbot/varshelper.txt)")


CMD_HELP.update({
    "dechahelper":
    "`.dechahelp`\
\nUsage: Bantuan Untuk Decha-Userbot.\
\n`.dechavar`\
\nUsage: Melihat Daftar Vars."
})
