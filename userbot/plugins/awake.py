#CREDITS = @LEGENDX22 @PROBOYX @alain_champion
#Special thanks @alain_champion for this modified version
#if you kang then keep credits
"""
import os
import time
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME, DARKLONversion, StartTime, CMD_HELP
from . import legend
from userbot.legend import BOT
from userbot.utils import admin_cmd, sudo_cmd
from telethon import version
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from platform import python_version, uname

ALIVE_PHOTTO = Config.ALIVE_PHOTTO
if ALIVE_PHOTTO is None:
  ALIVE_PHOTTO = https://telegra.ph/file/4678add619696c235a42a.jpg"


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "DARKLON"

global ghanti
        
#make by LEGEND X bht mehnat lag gayi yrr but banhi gaya 😅           
#@command(outgoing=True, pattern="^.awake$")
@borg.on(admin_cmd(pattern=r"awake")) 
@borg.on(sudo_cmd(pattern="awake ?(.*)", allow_sudo=True))
async def amireallyalive(awake):
   """ For .awake command, check if the bot is running.  """
   tag = borg.uid
   uptm = await legend.get_readable_time((time.time() - StartTime))
   ALIVE_MESSAGE= f" ⚡️ {BOT} ⚡️  IS ON 🔥 FIRE 🔥"
   ALIVE_MESSAGE += "\n\n"
   ALIVE_MESSAGE += "💟 𝚂𝚈𝚂𝚃𝙴𝙼 𝚂𝚃𝙰𝚃𝚄𝚂 💟\n\n"
   ALIVE_MESSAGE += "☎️ 𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 ☎️ : 1.19.5\n\n"
   ALIVE_MESSAGE += "🔶 DARKLON 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 🔶 :   0.0.1\n\n"
   ALIVE_MESSAGE += f"🔷 𝚄𝙿𝚃𝙸𝙼𝙴 🔷 : {uptm}\n\n"
   ALIVE_MESSAGE += f"💠 𝙼𝚈 𝙱𝙾𝚂𝚂 💠: {DEFAULTUSER} (tg://user?id=%7Btag%7D)\n\n"
   ALIVE_MESSAGE += "🔰 𝙶𝚁𝙾𝚄𝙿 🔰 : SUPPORT (https://t.me/DARKLON_USERBOT_SUPPORT)\n\n"
   ALIVE_MESSAGE += "⚡️ CHANNEL ⚡️ : CHANNEL (https://t.me/DARKLONXOP)\n\n"
   ALIVE_MESSAGE += "🔥 OT GROUP 🔥 : OT](https://t.me/DARKLON_OT\n\n"
   ALIVE_MESSAGE += f"💠 [𝙳𝙴𝙿𝙻𝙾𝚈 (https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FHACKERBOTTELEGRAM%2FDARKLON-PACK&template=https%3A%2F%2Fgithub.com%2FHACKERBOTTELEGRAM%2FDARKLON-PACK) 𝚈𝙾𝚄𝚁 𝙾𝚆𝙽 𝙾𝙿 {BOT} (https://github.com/HACKERBOTTELEGRAM/HACKERBOTOP)  💠\n"   
   await awake.delete() 
   await borg.send_file(awake.chat_id, ALIVE_PHOTTO,caption=ALIVE_MESSAGE)

CMD_HELP.update(
    {
        "awake": "Plugin : awake\
    \n\nSyntax : .awake\
    \nFunction : you can set here costom alive pic .set var ALIVE_PHOTTO (Telegraph link)"
    }
)
