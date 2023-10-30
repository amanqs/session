from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton(" sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴛʀɪɴɢ ", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text=" Kembali ", callback_data="home")]
    ]


    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅ", callback_data="help"),
            InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about")
        ],
        [InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/amangsupportgrup")],
    ]

    START = """
Halo {}
━━━━━━━━━━━━━━━━━━━━━━━━
{} di buat untuk Membantu anda Untuk 
Mengambil String Session Telegram 
dengan Mudah dan Aman Untuk id 5 & 6.
━━━━━━━━━━━━━━━━━━━━━━━━
Managed With ☕️ By @amwang
    """

    HELP = """
**✨ Perintah Yang Tersedia**

 × /start - Mulai Bot
 × /about - Tentang Bot ini
 × /help - bantuan
 × /generate - Mulai Pengambilan String
 × /cancel - Membatalkan Proses Pengambilan String
 × /restart - Merestart Proses Pengambilan String
"""

    ABOUT = """
**Tentang Bot ini** 

Amang String Bot di buat untuk Membantu anda Untuk
Mengambil String Session Telegram dengan
Simple dan Mudah!

 • Group Support: @amangsupportgrup
 • Framework: Pyrogram (https://docs.pyrogram.org/)
 • Language: Python (https://www.python.org/)

🖥 Develoved by @amwang
    """
