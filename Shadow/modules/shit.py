﻿from Shadow.decorator import register

from .utils.disable import disableable_dec


@register(cmds="jo")
@disableable_dec("jo")
async def _(message):
    j = "Hello there"
    await message.reply(j)


__mod_name__ = "jo"
__help__ = """
<b>jo</b>
- /jo: fuck of dude
"""
