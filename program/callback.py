# Copyright (C) 2021 By VeezMusicProject

from driver.core import me_bot
from driver.decorators import check_blacklist
from driver.queues import QUEUE
from pyrogram import Client, filters
from program.utils.inline import menu_markup, stream_markup
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from config import (
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_USERNAME,
    UPDATES_CHANNEL,
    SUDO_USERS,
    OWNER_ID,
)


@Client.on_callback_query(filters.regex("home_start"))
@check_blacklist()
async def start_set(_, query: CallbackQuery):
    BOT_NAME = me["first_name"]
    await query.answer("home start")
    await query.edit_message_text(
        f"""✨ **Welcome [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 [{BOT_NAME}](https://t.me/{BOT_USERNAME}) **Is a bot to play music and video in groups, through the Telegram Group video chat!**

💡 **لمعرفة جميع اوامر البوت اضغط علي » 📚 زرار الاوامر!**

🔖** لمعرفه طريقه استخدام اضغط علي كلمه  » ❓ زرار الدليل الاساسي!""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ اضفني الي مجموعتك ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ الدليل الاساسي", callback_data="user_guide")],
                [
                    InlineKeyboardButton("📚 الاوامر", callback_data="command_list"),
                    InlineKeyboardButton("❤ المالك", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 جروب الدعم", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 قناة السورس", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "𝒔𝒐𝒖𝒓𝒄𝒆 𝒑𝒂𝒓𝒊𝒔🇫🇷", url="https://t.me/belalelshayals"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("quick_use"))
@check_blacklist()
async def quick_set(_, query: CallbackQuery):
    await query.answer("quick bot usage")
    await query.edit_message_text(
        f"""ℹ️ Quick use Guide bot, please read fully !

شغل : لتشغيل الاغنيه
فيديو : لتشغيل فيديو + الجوده
لايف : لتشغيل لايف

❓ Have questions? Contact us in [Support Group](https://t.me/{GROUP_SUPPORT}).""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="command_list")]]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("user_guide"))
@check_blacklist()
async def guide_set(_, query: CallbackQuery):
    ass_uname = me["username"]
    await query.answer("user guide")
    await query.edit_message_text(
        f"""❓ How to use this Bot ?, read the Guide below !

1.) **اولا اضفني الى المجموعه.**
2.) **ثانيا ارفعني ادمن .الي المجموعه ثم رقيني ادمن .**
3.) **بعد الترقيه اكتب ريلود لاعاده تشغيل البوت بشكل جيد.**
3.) **ضيف @{ASSISTANT_NAME} حساب المساعد او اكتب انضم علشان يدخل .**
4.) **بعد لما تضيفه اكتب شغل لتشغيل اغاني او اكتب فيديو لتشغيل فيديو او لايغ .**
5.) **كل فتره اعمل ريلود علشان لو في خطا يتصلح.**

`- END, EVERYTHING HAS BEEN SETUP -`

📌 If the userbot not joined to video chat, make sure if the video chat already turned on and the userbot in the chat.

💡 If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}.""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="home_start")]]
        ),
    )


@Client.on_callback_query(filters.regex("command_list"))
@check_blacklist()
async def commands_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    await query.answer("commands menu")
    await query.edit_message_text(
        f"""✨ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» Check out the menu below to read the module information & see the list of available Commands !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("» Quick use Guide «", callback_data="quick_use"),
                ],[
                    InlineKeyboardButton("👷🏻 اوامر ادمن الجروب", callback_data="admin_command"),
                    InlineKeyboardButton("🧙🏻 اوامر المطور ", callback_data="user_command"),
                ],[
                    InlineKeyboardButton("اوامر المطور", callback_data="sudo_command"),
                    InlineKeyboardButton("اوامر المالك", callback_data="owner_command"),
                ],[
                    InlineKeyboardButton("🔙 Go Back", callback_data="home_start")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("user_command"))
@check_blacklist()
async def user_set(_, query: CallbackQuery):
    BOT_NAME = me["first_name"]
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""✏️ Command list for all user.

» شغل (song name/link) - play music on video chat
» فيديو (video name/link) - play video on video chat
» لايف - play live video from yt live/m3u8
» ابحث (query) - search a youtube video link
» playlist - see the current playing song
» lyric (query) - scrap the song lyric
» video (query) - download video from youtube
» song (query) - download song from youtube
» ping - show the bot ping status
» uptime - show the bot uptime status
» alive - show the bot alive info (in Group only)

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("admin_command"))
@check_blacklist()
async def admin_set(_, query: CallbackQuery):
    BOT_NAME = me["first_name"]
    await query.answer("admin commands")
    await query.edit_message_text(
        f"""✏️ Command list for group admin.

» وقف - pause the stream
» كمل - resume the stream
» تخطي - switch to next stream
»  ايقاف - stop the streaming
» /كتم - mute the userbot on voice chat
» الغاء كتم - unmute the userbot on voice chat
» الصوت `1-200` - adjust the volume of music (userbot must be admin)
» ريلود - reload bot and refresh the admin data
» انضم - invite the userbot to join group
» اخرج - order userbot to leave from group

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("sudo_command"))
@check_blacklist()
async def sudo_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    BOT_NAME = me["first_name"]
    if user_id not in SUDO_USERS:
        await query.answer("⚠️ You don't have permissions to click this button\n\n» This button is reserved for sudo members of this bot.", show_alert=True)
        return
    await query.answer("sudo commands")
    await query.edit_message_text(
        f"""✏️ Command list for sudo user.

» /stats - get the bot current statistic
» /calls - show you the list of all active group call in database
» /block (`chat_id`) - use this to blacklist any group from using your bot
» /unblock (`chat_id`) - use this to whitelist any group from using your bot
» /blocklist - show you the list of all blacklisted chat
» /speedtest - run the bot server speedtest
» /sysinfo - show the system information
» /eval - execute any code (`developer stuff`)
» /sh - run any command (`developer stuff`)

⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("owner_command"))
@check_blacklist()
async def owner_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    BOT_NAME = me["first_name"]
    if user_id not in OWNER_ID:
        await query.answer("⚠️ You don't have permissions to click this button\n\n» This button is reserved for owner of this bot.", show_alert=True)
        return
    await query.answer("owner commands")
    await query.edit_message_text(
        f"""✏️ Command list for bot owner.

» /gban (`username` or `user_id`) - for global banned people, can be used only in group
» /ungban (`username` or `user_id`) - for un-global banned people, can be used only in group
» /update - update your bot to latest version
» /restart - restart your bot directly
» /leaveall - order userbot to leave from all group
» /leavebot (`chat id`) - order bot to leave from the group you specify
» /broadcast (`message`) - send a broadcast message to all groups in bot database
» /broadcast_pin (`message`) - send a broadcast message to all groups in bot database with the chat pin

⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("stream_menu_panel"))
@check_blacklist()
async def at_set_markup_menu(_, query: CallbackQuery):
    user_id = query.from_user.id
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Only admin with manage video chat permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    if chat_id in QUEUE:
        await query.answer("control panel opened")
        await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("stream_home_panel"))
@check_blacklist()
async def is_set_home_menu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Only admin with manage video chat permission that can tap this button !", show_alert=True)
    await query.answer("control panel closed")
    user_id = query.message.from_user.id
    buttons = stream_markup(user_id)
    await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))


@Client.on_callback_query(filters.regex("set_close"))
@check_blacklist()
async def on_close_menu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Only admin with manage video chat permission that can tap this button !", show_alert=True)
    await query.message.delete()


@Client.on_callback_query(filters.regex("close_panel"))
@check_blacklist()
async def in_close_panel(_, query: CallbackQuery):
    await query.message.delete()
