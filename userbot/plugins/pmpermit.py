"""
Support chatbox for pmpermit.
Used by incoming messages with trigger as /start
Will not work for already approved people.
Credits: written by ༺αиυвιѕ༻ {@A_Dark_Princ3}
"""
import asyncio

from telethon import events, functions

import userbot.plugins.sql_helper.pmpermit_sql as pmpermit_sql

from . import ALIVE_NAME, PM_START, PMMESSAGE_CACHE, set_key

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "HACKEROP"
PREV_REPLY_MESSAGE = {}
PM = f"""Hello. You are accessing the availabe menu of my master, {DEFAULTUSER}.
__Let's make this smooth and let me know why you are here.__
**Choose one of the following reasons why you are here:**

`a`. To chat with my master
`b`. To spam my master's inbox.
`c`. To enquire something
`d`. To request something\n"""
ONE = """__Okay. Your request has been registered. Do not spam my master's inbox.You can expect a reply within next few years. He/She is a busy man, unlike you probably.__

**⚠️ You will be blocked and reported if you spam. ⚠️**\n\n"""
TWO = " `███████▄▄███████████▄  \n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓███░░░░░░░░░░░░█\n██████▀▀▀█░░░░██████▀  \n░░░░░░░░░█░░░░█  \n░░░░░░░░░░█░░░█  \n░░░░░░░░░░░█░░█  \n░░░░░░░░░░░█░░█  \n░░░░░░░░░░░░▀▀ `\n\n**So uncool, this is not your home. Go bother someone else. You have been blocked and reported until further notice.**"
THREE = "__Okay. My master has not seen your message yet.He/She usually responds to people,though idk about retarted ones.__\n __He'll respond when he/she comes back, if he/she wants to.There's already a lot of pending messages😶__\n **Please do not spam unless you wish to be blocked and reported.**"
FOUR = "`Okay. please have the basic manners as to not bother my master too much. If he/she wishes to help you, he/she will respond to you soon.`\n**Do not ask repeatdly else you will be blocked and reported.**"
LWARN = "**This is your last warning. DO NOT send another message else you will be blocked and reported. Keep patience. My master will respond you ASAP.**\n"


@bot.on(events.NewMessage(pattern=r"\/start", incoming=True))
async def _(event):
    if event.fwd_from:
        return
    chat_id = event.sender_id
    if not pmpermit_sql.is_approved(chat_id):
        chat = await event.get_chat()
        if chat_id not in PM_START:
            PM_START.append(chat_id)
        if not event.is_private:
            return
        set_key(PMMESSAGE_CACHE, event.chat_id, event.id)
        try:
            async with event.client.conversation(chat) as conv:
                if pmpermit_sql.is_approved(chat_id):
                    return
                test1 = await event.client.send_message(chat, PM)
                set_key(PMMESSAGE_CACHE, event.chat_id, test1.id)
                chat_id = event.sender_id
                response = await conv.get_response(chat)
                y = response.text
                if y == "a" or "A":
                    if pmpermit_sql.is_approved(chat_id):
                        return
                    set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                    test2 = await event.client.send_message(chat, ONE)
                    set_key(PMMESSAGE_CACHE, event.chat_id, test2.id)
                    response = await conv.get_response(chat)
                    if response.text != "/start":
                        if pmpermit_sql.is_approved(chat_id):
                            return
                        set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                        test3 = await event.client.send_message(chat, LWARN)
                        set_key(PMMESSAGE_CACHE, event.chat_id, test3.id)
                        response = await conv.get_response(chat)
                        if response.text != "/start":
                            if pmpermit_sql.is_approved(chat_id):
                                return
                            set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                            test4 = await event.client.send_message(chat, TWO)
                            set_key(PMMESSAGE_CACHE, event.chat_id, test4.id)
                            await asyncio.sleep(3)
                            await event.client(functions.contacts.BlockRequest(chat_id))
                elif y == "b" or "B":
                    if pmpermit_sql.is_approved(chat_id):
                        return
                    set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                    test5 = await event.client.send_message(chat, LWARN)
                    set_key(PMMESSAGE_CACHE, event.chat_id, test5.id)
                    response = await conv.get_response(chat)
                    if response.text != "/start":
                        if pmpermit_sql.is_approved(chat_id):
                            return
                        set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                        test6 = await event.client.send_message(chat, TWO)
                        set_key(PMMESSAGE_CACHE, event.chat_id, test6.id)
                        await asyncio.sleep(3)
                        await event.client(functions.contacts.BlockRequest(chat_id))
                elif y == "c" or "C":
                    if pmpermit_sql.is_approved(chat_id):
                        return
                    set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                    test7 = await event.client.send_message(chat, THREE)
                    set_key(PMMESSAGE_CACHE, event.chat_id, test7.id)
                    response = await conv.get_response(chat)
                    if response.text != "/start":
                        if pmpermit_sql.is_approved(chat_id):
                            return
                        set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                        test8 = await event.client.send_message(chat, LWARN)
                        set_key(PMMESSAGE_CACHE, event.chat_id, test8.id)
                        response = await conv.get_response(chat)
                        if response.text != "/start":
                            if pmpermit_sql.is_approved(chat_id):
                                return
                            set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                            test9 = await event.client.send_message(chat, TWO)
                            set_key(PMMESSAGE_CACHE, event.chat_id, test9.id)
                            await asyncio.sleep(3)
                            await event.client(functions.contacts.BlockRequest(chat_id))
                elif y == "d" or "D":
                    if pmpermit_sql.is_approved(chat_id):
                        return
                    set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                    test10 = await event.client.send_message(chat, FOUR)
                    set_key(PMMESSAGE_CACHE, event.chat_id, test10.id)
                    response = await conv.get_response(chat)
                    if response.text != "/start":
                        if pmpermit_sql.is_approved(chat_id):
                            return
                        set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                        test11 = await event.client.send_message(chat, LWARN)
                        set_key(PMMESSAGE_CACHE, event.chat_id, test11.id)
                        response = await conv.get_response(chat)
                        if response.text != "/start":
                            if pmpermit_sql.is_approved(chat_id):
                                return
                            set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                            await event.client.send_message(chat, TWO)
                            await asyncio.sleep(3)
                            await event.client(functions.contacts.BlockRequest(chat_id))
                else:
                    if pmpermit_sql.is_approved(chat_id):
                        return
                    test12 = await event.client.send_message(
                        chat,
                        "You have entered an invalid command. Please send `/start` again or do not send another message if you do not wish to be blocked and reported.",
                    )
                    set_key(PMMESSAGE_CACHE, event.chat_id, test12.id)
                    response = await conv.get_response(chat)
                    z = response.text
                    if z != "/start":
                        if pmpermit_sql.is_approved(chat_id):
                            return
                        set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                        test13 = await event.client.send_message(chat, LWARN)
                        set_key(PMMESSAGE_CACHE, event.chat_id, test13.id)
                        response = await conv.get_response(chat)
                        if response.text != "/start":
                            if pmpermit_sql.is_approved(chat_id):
                                return
                            set_key(PMMESSAGE_CACHE, event.chat_id, response.id)
                            test14 = await event.client.send_message(chat, TWO)
                            set_key(PMMESSAGE_CACHE, event.chat_id, test14.id)
                            await asyncio.sleep(3)
                            await event.client(functions.contacts.BlockRequest(chat_id))
        except Exception as e:
            LOGS.info(str(e))

import asyncio

from telethon import events, functions

from . import (
    ALIVE_NAME,
    PM_START,
    PMMENU,
    PMMESSAGE_CACHE,
    check,
    get_user_from_event,
    parse_pre,
    set_key,
)
from .sql_helper import pmpermit_sql as pmpermit_sql

PM_WARNS = {}
PREV_REPLY_MESSAGE = {}
CACHE = {}
PMPERMIT_PIC = Config.PMPERMIT_PIC
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "HACKEROP"
USER_BOT_WARN_ZERO = "You were spamming my peru master's inbox, henceforth you are blocked by my master's userbot. **Now GTFO, i'm playing minecraft** "


if Config.PRIVATE_GROUP_ID != 0:

    @bot.on(admin_cmd(outgoing=True))
    async def you_dm_niqq(event):
        if event.fwd_from:
            return
        chat = await event.get_chat()
        if event.text.startswith((".block", ".disapprove", ".a", ".da", ".approve")):
            return
        if (
            event.is_private
            and not pmpermit_sql.is_approved(chat.id)
            and chat.id not in PM_WARNS
        ):
            pmpermit_sql.approve(chat.id, "outgoing")

    @bot.on(admin_cmd(pattern="(a|approve)(?: |$)(.*)"))
    async def approve_p_m(event):
        if event.is_private:
            user = await event.get_chat()
            reason = event.pattern_match.group(1)
        else:
            user, reason = await get_user_from_event(event, secondgroup=True)
            if not user:
                return
            if not reason:
                reason = "Not mentioned"
        if not pmpermit_sql.is_approved(user.id):
            if user.id in PM_WARNS:
                del PM_WARNS[user.id]
            if user.id in PREV_REPLY_MESSAGE:
                await PREV_REPLY_MESSAGE[user.id].delete()
                del PREV_REPLY_MESSAGE[user.id]
            if user.id in PM_START:
                PM_START.remove(user.id)
            pmpermit_sql.approve(user.id, reason)
            await edit_delete(
                event,
                f"`Approved to pm `[{user.first_name}](tg://user?id={user.id})",
                5,
            )
            if user.id in PMMESSAGE_CACHE:
                try:
                    await event.client.delete_messages(
                        user.id, PMMESSAGE_CACHE[user.id]
                    )
                except Exception as e:
                    LOGS.info(str(e))
        else:
            await edit_delete(
                event,
                f"[{user.first_name}](tg://user?id={user.id}) `is already in approved list`",
                5,
            )

    @bot.on(admin_cmd(pattern="(da|disapprove)(?: |$)(.*)"))
    async def disapprove_p_m(event):
        if event.is_private:
            user = await event.get_chat()
        else:
            input_str = event.pattern_match.group(2)
            if input_str == "all":
                return
            user, reason = await get_user_from_event(event, secondgroup=True)
            if reason == "all":
                return
            if not user:
                return
        if user.id in PM_START:
            PM_START.remove(user.id)
        if pmpermit_sql.is_approved(user.id):
            pmpermit_sql.disapprove(user.id)
            await edit_or_reply(
                event,
                f"`disapproved to pm` [{user.first_name}](tg://user?id={user.id})",
            )
        else:
            await edit_or_reply(
                event,
                f"[{user.first_name}](tg://user?id={user.id}) `is not yet approved`",
                5,
            )

    @bot.on(admin_cmd(pattern="block(?: |$)(.*)"))
    async def block_p_m(event):
        if event.is_private:
            user = await event.get_chat()
        else:
            user, reason = await get_user_from_event(event)
            if not user:
                return
        if user.id in PM_START:
            PM_START.remove(user.id)
        await event.edit(
            f"`You are blocked Now .You Can't Message Me from now..`[{user.first_name}](tg://user?id={user.id})"
        )
        await event.client(functions.contacts.BlockRequest(user.id))

    @bot.on(admin_cmd(pattern="unblock(?: |$)(.*)"))
    async def unblock_pm(event):
        if event.is_private:
            user = await event.get_chat()
        else:
            user, reason = await get_user_from_event(event)
            if not user:
                return
        await event.client(functions.contacts.UnblockRequest(user.id))
        await event.edit(
            f"`You are Unblocked Now .You Can Message Me From now..`[{user.first_name}](tg://user?id={user.id})"
        )

    @bot.on(admin_cmd(pattern="listapproved$"))
    async def approve_p_m(event):
        approved_users = pmpermit_sql.get_all_approved()
        APPROVED_PMs = "Current Approved PMs\n"
        if len(approved_users) > 0:
            for sender in approved_users:
                if sender.reason:
                    APPROVED_PMs += f"👉 [{sender.chat_id}](tg://user?id={sender.chat_id}) for {sender.reason}\n"
                else:
                    APPROVED_PMs += (
                        f"👉 [{sender.chat_id}](tg://user?id={sender.chat_id})\n"
                    )
        else:
            APPROVED_PMs = "`You havent approved anyone yet`"
        await edit_or_reply(
            event,
            APPROVED_PMs,
            file_name="approvedpms.txt",
            caption="`Current Approved PMs`",
        )

    @bot.on(admin_cmd(pattern="(disapprove all|da all)$"))
    async def disapprove_p_m(event):
        if event.fwd_from:
            return
        result = "`ok , everyone is disapproved now`"
        pmpermit_sql.disapprove_all()
        await edit_delete(event, result, parse_mode=parse_pre, time=10)

    @bot.on(events.NewMessage(incoming=True))
    async def on_new_private_message(event):
        if event.sender_id == event.client.uid:
            return
        if Config.PRIVATE_GROUP_ID is None:
            return
        if not event.is_private:
            return
        chat_id = event.sender_id
        if chat_id in CACHE:
            sender = CACHE[chat_id]
        else:
            sender = await event.get_chat()
            CACHE[chat_id] = sender
        if sender.bot or sender.verified:
            return
        if PMMENU:
            if event.raw_text == "/start":
                if chat_id not in PM_START:
                    PM_START.append(chat_id)
                set_key(PMMESSAGE_CACHE, event.chat_id, event.id)
                return
            if len(event.raw_text) == 1 and check(event.raw_text):
                set_key(PMMESSAGE_CACHE, event.chat_id, event.id)
                return
            if chat_id in PM_START:
                return
        if not pmpermit_sql.is_approved(chat_id):
            await do_pm_permit_action(chat_id, event, sender)

    async def do_pm_permit_action(chat_id, event, sender):
        if chat_id not in PM_WARNS:
            PM_WARNS.update({chat_id: 0})
        if PM_WARNS[chat_id] == Config.MAX_FLOOD_IN_PMS:
            r = await event.reply(USER_BOT_WARN_ZERO)
            await asyncio.sleep(1)
            await event.client(functions.contacts.BlockRequest(chat_id))
            if chat_id in PREV_REPLY_MESSAGE:
                await PREV_REPLY_MESSAGE[chat_id].delete()
            if chat_id in PM_START:
                PM_START.remove(chat_id)
            PREV_REPLY_MESSAGE[chat_id] = r
            the_message = f"#BLOCKED_PMs\
                            \n[User](tg://user?id={chat_id}) : {chat_id}\
                            \nMessage Count: {PM_WARNS[chat_id]}"
            try:
                await event.client.send_message(
                    entity=Config.PRIVATE_GROUP_ID,
                    message=the_message,
                )
                return
            except BaseException:
                return
        me = await event.client.get_me()
        mention = f"[{sender.first_name}](tg://user?id={sender.id})"
        my_mention = f"[{me.first_name}](tg://user?id={me.id})"
        first = sender.first_name
        last = sender.last_name
        fullname = f"{first} {last}" if last else first
        username = f"@{sender.username}" if sender.username else mention
        userid = sender.id
        my_first = me.first_name
        my_last = me.last_name
        my_fullname = f"{my_first} {my_last}" if my_last else my_first
        my_username = f"@{me.username}" if me.username else my_mention
        totalwarns = Config.MAX_FLOOD_IN_PMS + 1
        warns = PM_WARNS[chat_id] + 1
        if PMMENU:
            if Config.CUSTOM_PMPERMIT_TEXT:
                USER_BOT_NO_WARN = (
                    Config.CUSTOM_PMPERMIT_TEXT.format(
                        mention=mention,
                        first=first,
                        last=last,
                        fullname=fullname,
                        username=username,
                        userid=userid,
                        my_first=my_first,
                        my_last=my_last,
                        my_fullname=my_fullname,
                        my_username=my_username,
                        my_mention=my_mention,
                        totalwarns=totalwarns,
                        warns=warns,
                    )
                    + "\n\n"
                    + "**Send** `/start` ** so that my master can decide why you're here.**"
                )
            else:

                USER_BOT_NO_WARN = (
                    f"`Hi `{mention}`, I haven't approved you yet to personal message me, Don't spam my inbox."
                    f"Just say the reason and wait until you get approved.\
                                    \n\nyou have {warns}/{totalwarns} warns`\
                                    \n\n**Send** `/start` **so that my master can decide why you're here.**"
                )
        else:
            if Config.CUSTOM_PMPERMIT_TEXT:
                USER_BOT_NO_WARN = Config.CUSTOM_PMPERMIT_TEXT.format(
                    mention=mention,
                    first=first,
                    last=last,
                    fullname=fullname,
                    username=username,
                    userid=userid,
                    my_first=my_first,
                    my_last=my_last,
                    my_fullname=my_fullname,
                    my_username=my_username,
                    my_mention=my_mention,
                    totalwarns=totalwarns,
                    warns=warns,
                )
            else:
                USER_BOT_NO_WARN = (
                    f"`Hi `{mention}`, I haven't approved you yet to personal message me, Don't spam my inbox."
                    f"Just say the reason and wait until you get approved.\
                                    \n\nyou have {warns}/{totalwarns} warns`"
                )
        if PMPERMIT_PIC:
            r = await event.reply(USER_BOT_NO_WARN, file=PMPERMIT_PIC)
        else:
            r = await event.reply(USER_BOT_NO_WARN)
        PM_WARNS[chat_id] += 1
        if chat_id in PREV_REPLY_MESSAGE:
            await PREV_REPLY_MESSAGE[chat_id].delete()
        PREV_REPLY_MESSAGE[chat_id] = r
        return None


CMD_HELP.update(
    {
        "pmpermit": "**Plugin : **`pmpermit`\
        \n\n  •  **Syntax : **`.approve or .a`\
        \n  •  **Function : **__Approves the mentioned/replied person to PM.__\
        \n\n  •  **Syntax : **`.disapprove or .da`\
        \n  •  **Function : **__dispproves the mentioned/replied person to PM.__\
        \n\n  •  **Syntax : **`.block`\
        \n  •  **Function : **__Blocks the person.__\
        \n\n  •  **Syntax : **`.unblock`\
        \n  •  **Function : **__Unblocks the person.__\
        \n\n  •  **Syntax : **`.listapproved`\
        \n  •  **Function : **__To list the all approved users.__\
        \n\n  •  **Syntax : **`.disapprove all or da all`\
        \n  •  **Function : **__To disapprove all the approved users.__\
        \n\n  •  Available variables for formatting `CUSTOM_PMPERMIT_TEXT` :\
        \n`{mention}`, `{first}`, `{last} `, `{fullname}`, `{userid}`, `{username}`, `{my_first}`, `{my_fullname}`, `{my_last}`, `{my_mention}`, `{my_username}`,`{warns}` , `{totalwarns}`.\
"
    }
)
