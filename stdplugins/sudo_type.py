"""Typewriter 
Syntax: .type Query
Made by @meanii 
Please Don't remove credit name 
"""
import asyncio
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="type (.*)",allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    # https://t.me/AnotherGroup/176551
    input_str = event.pattern_match.group(1)
    shiiinabot = "\u2060"
    for i in range(601):
        shiiinabot += "\u2060"
    try:
        await event.delete()
        process = await event.reply(shiiinabot)
        await process.edit(shiiinabot)
    except Exception as e:
        logger.warn(str(e))
    typing_symbol = "|"
    DELAY_BETWEEN_EDITS = 0.3
    previous_text = ""
    await process.edit(typing_symbol)
    await asyncio.sleep(DELAY_BETWEEN_EDITS)
    for character in input_str:
        previous_text = previous_text + "" + character
        typing_text = previous_text + "" + typing_symbol
        try:
            await process.edit(typing_text)
        except Exception as e:
            logger.warn(str(e))
            pass
        await asyncio.sleep(DELAY_BETWEEN_EDITS)
        try:
            await process.edit(previous_text)
        except Exception as e:
            logger.warn(str(e))
            pass
        await asyncio.sleep(DELAY_BETWEEN_EDITS)
