"""
.log to view bot log
For SUDO USER
"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="log"))
@borg.on(events.NewMessage(pattern=r"\.log(.*)",incoming=True))
async def _(event):
    if event.fwd_from:
        return
    mentions = "**αℓℓυкα Zᴏʟᴅʏᴄᴋ™** //logs\n👉🏻Fix `.kang` double reply.\n👉🏻Added new plugin `.count` To view my stats 😉 **FOR SUDO USER ONLY**"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()
