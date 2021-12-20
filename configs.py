# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Rename-Bot-0")
    SLEEP_TIME = int(os.environ.get("SLEEP_TIME", 5))
    BOT_OWNER = os.environ.get("BOT_OWNER", 1287407305)
    CAPTION = "Rename Bot by @{}\n\nMade by @KDramasFlix"
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -100))
    MONGODB_URI = os.environ.get("MONGODB_URI", "")
    DOWNLOAD_PATH = os.environ.get("DOWNLOAD_PATH", "./downloads")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    ONE_PROCESS_ONLY = bool(os.environ.get("ONE_PROCESS_ONLY", False))
    START_TEXT = """
This is Telegram File Renameing Bot.

Send me any type of media  or File to Rename it .

Made with ❤ by @TeleRoidGroup.
    """
    HELP_TELEROID = """
<i>𝐖𝐚𝐭𝐜𝐡 𝐕𝐢𝐝𝐞𝐨 𝐇𝐨𝐰 𝐭𝐨 𝐔𝐬𝐞 𝐌𝐞 <a href='https://youtu.be/HnXdu74o34E'>[ ᴄʟɪᴄᴋ ʜᴇʀᴇ ]</a></i>\n
<i>𝐒𝐞𝐧𝐝 𝐚 𝐩𝐡𝐨𝐭𝐨 𝐭𝐨 𝐦𝐚𝐤𝐞 𝐢𝐭 𝐚𝐬 𝐭𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 (optional)</i>\n
<i>𝐒𝐞𝐧𝐝 𝐦𝐞 𝐚𝐧𝐲 𝐟𝐢𝐥𝐞 (or) 𝐌𝐞𝐝𝐢𝐚 𝐟𝐫𝐨𝐦 𝐭𝐞𝐥𝐞𝐠𝐫𝐚𝐦</i>\n
<i>𝐂𝐨𝐧𝐯𝐞𝐫𝐭 𝐟𝐢𝐥𝐞𝐬 𝐢𝐧𝐭𝐨 𝐯𝐢𝐝𝐞𝐨 𝐮𝐬𝐞 /settings 𝐜𝐨𝐦𝐦𝐚𝐧𝐝</i>\n
<i>just send the new files to rename it.ext</i>\n
<i>𝐕𝐢𝐞𝐰 𝐲𝐨𝐮𝐫 𝐭𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐝𝐨 /show_thumb 𝐜𝐨𝐦𝐦𝐚𝐧𝐝</i>\n
<i>𝐃𝐞𝐥𝐞𝐭𝐞 𝐲𝐨𝐮𝐫 𝐭𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐝𝐨 /delthumb 𝐜𝐨𝐦𝐦𝐚𝐧𝐝</i>
    """
    ABOUT_TELEROID = """
This is a Renamer bOt with Permanent Thumbnail Support. 
Send Me any Media or File I can Rename It. 
╭────[**🔅@RenamerXDBot🔅**]────⍟
│
├🤖**My Name:**[@RenamerDBot](https://t.me/{BOT_USERNAME})
│
├📝**Language:**[Python3](https://www.python.org)
│
├📚**Library:**[Pyrogram](https://docs.pyrogram.org)
│
├📡**Hosted On:**[Heorku](https://heroku.com)
│
├👨‍💻**Developer:**[@Predator](https://t.me/PredatorHackerzZ) 
│
├👥**Bot Support:**[Support](https://t.me/TeleRoid14)
│
├🔔**Bot Updates:**[Channel](https://t.me/TeleRoidGroup)
│
╰──────[ 😎 ]───────────⍟
    """
    PROGRESS = """\n
╭───[**🔅Progress Bar🔅**]───⍟
│
├<b>📁 : {1}</b>
│
├<b>✅ : {2}</b>
│
├<b>🚀 : {0}%</b>
│
├<b>⚡ : {3}/s</b>
│
├<b>⏱️ : {4}</b>
╰─────────────────⍟"""
