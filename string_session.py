#!/usr/bin/env python3

from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("""Kunjungi my.telegram.org
Login Menggunakan Akun Telegram Anda
Klik API Development Tools
Create a new application, 
Cek Telegram Saved Messages Lalu Copy STRING_SESSION""")
API_KEY = int(input("Masukkan API_KEY disini: "))
API_HASH = input("Masukkan API_HASH disini: ")

with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
    print("STRING_SESSION Sudah Dikirim Ke Save Message Telegram Anda")
    session_string = client.session.save()
    saved_messages_template = """

<code>STRING_SESSION DECHA USERBOT</code>: <code>{}</code>

⚠️ <i>Jangan Memberikan Kode Ini Kepada Orang Lain</i>""".format(session_string)
    client.send_message("me", saved_messages_template, parse_mode="html")
