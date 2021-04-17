#MADE BY @GODBOYX
#THANKS TO @LEGENDX22
#TEAMLEGEND
import asyncio
import random
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "DARKLON USER"

edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/09eed9cdb0a03be132bd2.jpg"
file2 = "https://telegra.ph/file/5c6554015d31075fd5eed.jpg"
file3 = "https://telegra.ph/file/2a1012b4d4604117a5ea3.jpg"
file4 = "https://telegra.ph/file/b6df6b2386397e03a8784.jpg"
file5 = "https://telegra.ph/file/2b22e380a0eabb414d9b1.jpg"
""" =======================CONSTANTS====================== """
pm_caption = "🔥🔥 DARKLON ɨֆ օռʟɨռɛ..!! 🔥🔥\n\n"
pm_caption += "⚔️⚔️ Yes Master, Am Alive And Systems Are Working Perfectly As It Should Be...⚔️⚔️\n\n"
pm_caption += "◆◆◆About My System◆◆◆\n\n"
pm_caption += "●●Telethon∆Version●● : 1.19.5\n'
pm_caption += f"●●Darklon∆User●●>> {DEFAULTUSER}\n"
pm_caption += "●●Darklon∆Version●● : 0.0.1\n"
pm_caption += "●●Support∆Group●● : [GROUP](https://t.me/DARKLON_USERBOT_SUPPORT\n"
pm_caption += "●●For Updates About Userbot●● : [CHANNEL](https://t.me/DARKLONXOP\n"
@borg.on(admin_cmd(pattern=r"alive"))

async def amireallyalive(yes):
    chat = await yes.get_chat()

    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)
    
    await asyncio.sleep(edit_time)
    ok8 = await borg.edit_message(yes.chat_id, ok7, file=file5)

    await alive.delete()
    
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()
