"""
RadioPlayerV2, Telegram Voice Chat Userbot
Copyright (C) 2021  Sadew Jayasekara

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

from pyrogram import Client, filters, emoji
from pyrogram.types import Message
from utils.vc import mp, RADIO
from config import Config
STREAM_URL=Config.STREAM_URL
ADMINS=Config.ADMINS

@Client.on_message(filters.command("صوت") & filters.user(ADMINS))
async def radio(client, message: Message):
    if 1 in RADIO:
        await message.reply_text(f"{emoji.ROBOT} **يرجى إيقاف تدفق الراديو الحالي عن طريق / توقف Command!**")
        return
    await mp.start_radio()
    await message.reply_text(f"{emoji.CHECK_MARK_BUTTON} **بدأ دفق الراديو :** \n<code>{STREAM_URL}</code>")

@Client.on_message(filters.command("توقف") & filters.user(ADMINS))
async def stop(_, message: Message):
    if 0 in RADIO:
        await message.reply_text(f"{emoji.ROBOT} **يرجى بدء تشغيل راديو أولاً بواسطة / أمر راديو!**")
        return
    await mp.stop_radio()
    await message.reply_text(f"{emoji.CROSS_MARK_BUTTON} **Radio Stream Ended Successfully!**")
