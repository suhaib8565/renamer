# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Rename-Bot-0")
    SLEEP_TIME = int(os.environ.get("SLEEP_TIME", 5))
    BOT_OWNER = os.environ.get("BOT_OWNER", 1445283714)
    CAPTION = "Rename Bot by @{}\n\nMade by @AbirHasan2005"
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
