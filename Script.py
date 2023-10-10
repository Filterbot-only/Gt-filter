import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    HOME_BUTTONURL_UPDATES = environ.get("HOME_BUTTONURL_UPDATES", 'https://t.me/QTVS_BOT_X_CLOUD')
    START_TXT = environ.get("START_TXT", '''<b>𝙷𝙴𝙻𝙻𝙾... {}
    
𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂  <a href=http://t.me/Gt_filter_bot>🦞𝐆𝐭 𝐅𝐢𝐥𝐭𝐞𝐫𝐳🌿<b></b></a>

𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙼𝙰𝙺𝙴 𝙼𝙴 𝙰𝙳𝙼𝙸𝙽.. 𝚃𝙷𝙴𝙽 𝚂𝙴𝙴 𝙼𝚈 𝙿𝙾𝚆𝙴𝚁𝚂

ᴍᴀᴅᴇ ᴡɪᴛʜ 🍁 ʙʏ <a href=https://t.me/SMD_Owner><b>🍁𝐀𝐮𝐭𝐡𝐨𝐫🌿</b></a></b>''')
    HELP_TXT = """ʜᴇʏ {}
ʜᴇʀᴇ ɪꜱ ᴍʏ ᴄᴏᴍᴍᴀɴᴅꜱ."""
    ABOUT_TXT = """<b>
╭────[ 𝐐𝐭𝐯𝐬𝐨𝐟𝐢𝐜𝐢𝐚𝐥 ]────⍟
│
├⍟ 𝐌𝐲 𝐍𝐚𝐦𝐞: <a href=http://t.me/Gt_filter_bot><b>🦂𝐆𝐭 𝐅𝐢𝐥𝐭𝐞𝐫𝐳♠</b></a>
├⍟ 𝐀𝐮𝐭𝐡𝐨𝐫 : <a href=https://t.me/Gowthamtn29><b>🦞𝐀𝐝𝐦𝐢𝐧🍁</b></a>
├⍟ 𝐏𝐞𝐚𝐜𝐞 : <a href=https://t.me/Gowthamtn29><b>❄𝐎𝐰𝐧𝐞𝐫🦞</b></a>
├⍟ 𝐏𝐫𝐨𝐣𝐞𝐜𝐭 : <a href=https://t.me/Gowthamtn29><b>💐𝐔𝐬𝐞𝐫❤‍🔥</b></a>
├⍟ 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞 : <a href=https://t.me/Gowthamtn29><b>🦞𝐒𝐮𝐩𝐩𝐨𝐫𝐭☠️</b></a>
├⍟ 𝐀𝐭𝐥𝐚𝐬𝐃𝐛 : <a href=https://t.me/Gowthamtn29><b>💖𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦😈</b></a>
├⍟ 𝐂𝐫𝐞𝐚𝐭𝐨𝐫 : <a href=https://t.me/Gowthamtn29><b>🌿𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞🥴</b></a>
├⍟ 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 : <a href=https://t.me/SMD_Owner><b>🎋𝐂𝐨𝐝𝐞𝐫♠</b></a>
│
╰─────────────────────⍟<b>"""
    SOURCE_TXT = """<b>𝐂𝐫𝐞𝐚𝐭𝐞 𝐎𝐧𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 💗
» ɪ ᴡɪʟʟ ᴄʀᴇᴀᴛᴇ ᴀ ʙᴏᴛ ꜰᴏʀ ʏᴏᴜ
» ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ @SMD_Owner</b>"""
    MANUELFILTER_TXT = """ʜᴇʟᴩ: <b>ꜰɪʟᴛᴇʀꜱ</b>

• ꜰɪʟᴛᴇʀ ɪꜱ ᴛʜᴇ ꜰᴇᴀᴛᴜʀᴇ ᴡᴇʀᴇ ᴜꜱᴇʀꜱ ᴄᴀɴ ꜱᴇᴛ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ʀᴇᴘʟɪᴇꜱ ꜰᴏʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴋᴇʏᴡᴏʀᴅ ᴀɴᴅ ᴡɪʟʟ ʀᴇꜱᴘᴏɴᴅ ᴡʜᴇɴᴇᴠᴇʀ ᴀ ᴋᴇʏᴡᴏʀᴅ ɪꜱ ꜰᴏᴜɴᴅ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ

<b>ɴᴏᴛᴇ:</b>
1. ꜰʟɪᴍꜱ ꜱʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
2. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ.
3. ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏꜰ 64 ᴄʜᴀʀᴀᴄᴛᴇʀꜱ.

<b>ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- MS Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Hb_LinkZzz supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/SMD_Owner)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of @Binthu_x_robot

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """🗽★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
❤‍🔥★ 𝐓𝐨𝐭𝐚𝐥 𝐔𝐬𝐞𝐫𝐬: <code>{}</code>
❤‍🔥★ 𝐓𝐨𝐭𝐚𝐥 𝐂𝐡𝐚𝐭𝐬: <code>{}</code>
❤‍🔥★ 𝐔𝐬𝐞𝐝 𝐒𝐭𝐨𝐫𝐚𝐠𝐞: <code>{}</code> 𝙼𝚒𝙱
❤‍🔥★ 𝐅𝐫𝐞𝐞 𝐒𝐭𝐨𝐫𝐚𝐠𝐞: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#𝐍𝐞𝐰𝐆𝐫𝐨𝐮𝐩
    
<b>᚛› 𝐆𝐫𝐨𝐮𝐩 ⪼ {}(<code>{}</code>)</b>
<b>᚛› 𝐓𝐨𝐭𝐚𝐥 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 ⪼ <code>{}</code></b>
<b>᚛› 𝐀𝐝𝐝𝐞𝐝 𝐁𝐲 ⪼ {}</b>
<b>᚛› @SMD_Owner </b>
"""
    LOG_TEXT_P = """#𝐍𝐞𝐰𝐔𝐬𝐞𝐫-new 
    
<b>᚛› 𝐈𝐃⚡ - <code>{}</code></b>
<b>᚛› 𝐍𝐚𝐦𝐞⚡ - {}</b>
<b>᚛› 𝐆𝐭 𝐅𝐢𝐥𝐭𝐞𝐫 </b>
"""
