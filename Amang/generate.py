import asyncio
from telethon import TelegramClient
from pyrogram.types import Message
from pyrogram import Client, filters
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)

from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)
from env import API_ID, API_HASH
from data import Data


ask_ques = "<b>String Session Mana Yang ingin anda Buat?</b>"
buttons_ques = [
    [
        InlineKeyboardButton("ᴘʏʀᴏɢʀᴀᴍ", callback_data="pyrogram"),
        InlineKeyboardButton("ᴛᴇʟᴇᴛʜᴏɴ", callback_data="telethon"),
    ],

]


@Client.on_message(filters.private & ~filters.forwarded & filters.command('generate'))
async def main(_, msg):
    await msg.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))


async def generate_session(bot: Client, msg: Message, telethon=False, is_bot: bool = False):
    if telethon:
        ty = "Telethon"
    else:
        ty = "Pyrogram v2"
    if is_bot:
        ty += " Bot"
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, 'Please send your `API_ID`', filters=filters.text)
    if await cancelled(api_id_msg):
        return
    try:
        api_id = int(api_id_msg.text)
    except ValueError:
        await api_id_msg.reply('Not a valid API_ID (which must be an integer). Please start generating session again.', quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    api_hash_msg = await bot.ask(user_id, 'Please send your `API_HASH`', filters=filters.text)
    if await cancelled(api_hash_msg):
        return
    api_hash = api_hash_msg.text
    if not is_bot:
        t = "**Silahkan Masukkan Nomor Telepon Telegram Anda Dengan Format Kode Negara.** \n**Contoh: +628xnxx**"
    else:
        t = "Now please send your `BOT_TOKEN` \nExample : `12345:abcdefghijklmnopqrstuvwxyz`'"
    phone_number_msg = await bot.ask(user_id, t, filters=filters.text)
    if await cancelled(phone_number_msg):
        return
    phone_number = phone_number_msg.text
    if not is_bot:
        await msg.reply("**Mengirim Kode OTP...**")
    else:
        await msg.reply("**Mengirim Kode OTP...**")
    if telethon and is_bot:
        client = TelegramClient(StringSession(), api_id=api_id, api_hash=api_hash)
    elif telethon:
        client = TelegramClient(StringSession(), api_id=api_id, api_hash=api_hash)
    elif is_bot:
        client = Client(name=f"bot_{user_id}", api_id=api_id, api_hash=api_hash, bot_token=phone_number, in_memory=True)
    else:
        client = Client(name=f"user_{user_id}", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()
    try:
        code = None
        if not is_bot:
            if telethon:
                code = await client.send_code_request(phone_number)
            else:
                code = await client.send_code(phone_number)
    #except (ApiIdInvalid, ApiIdInvalidError):
        #await msg.reply('`API_ID` and `API_HASH` combination is invalid. Please start generating session again.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        #return
    except (PhoneNumberInvalid, PhoneNumberInvalidError):
        await msg.reply('**NOMOR_TELEPON Yang anda masukan salah atau tidak terdaftar\nHarap Gunakan Format Kode Negara. Contoh: +628xnxx\n\nSilakan mulai membuat sesi lagi.**', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    try:
        phone_code_msg = None
        if not is_bot:
            phone_code_msg = await bot.ask(user_id, "**Silakan Periksa Kode OTP dari Akun Telegram Resmi.\nJika Kode OTP adalah 12345 Tolong [ TAMBAHKAN SPASI ] kirimkan Seperti ini 1 2 3 4 5** \n **Gunakan /cancel untuk Membatalkan Proses Pengambilan String!.**", filters=filters.text, timeout=600)
            if await cancelled(phone_code_msg):
                return
    except TimeoutError:
        await msg.reply('**membatalkan proses pengambilan string karena\nlimit waktu terlampaui.**', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
        try:
            if telethon:
                await client.sign_in(phone_number, phone_code, password=None)
            else:
                await client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeInvalidError):
            await msg.reply('**Kode OTP Yang anda masukan Tidak ditambahkan SPASI atau KODE OTP sudah kadaluarsa. Silakan mulai membuat sesi lagi.**', reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError):
            await msg.reply('**Kode OTP Yang anda masukan Tidak ditambahkan SPASI atau KODE OTP sudah kadaluarsa. Silakan mulai membuat sesi lagi.**', reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError):
            try:
                two_step_msg = await bot.ask(user_id, '**Akun anda Telah mengaktifkan Verifikasi Dua Langkah. Silahkan Kirimkan Passwordnya.**', filters=filters.text, timeout=300)
            except TimeoutError:
                await msg.reply('**membatalkan proses pengambilan string karena\nlimit waktu terlampaui.**', reply_markup=InlineKeyboardMarkup(Data.generate_button))
                return
            try:
                salah = await msg.reply("**Berhasil Membuat String Session**")
                password = two_step_msg.text
                if telethon:
                    await client.sign_in(password=password)
                else:
                    await client.check_password(password=password)
                if await cancelled(salah):
                    return
            except (PasswordHashInvalid, PasswordHashInvalidError):
                await two_step_msg.reply('**Kata Sandi yang Diberikan Tidak Valid. Silakan mulai membuat sesi lagi.**', quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
                return
    else:
        if telethon:
            await client.start(bot_token=phone_number)
        else:
            await client.sign_in_bot(phone_number)
    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()
    text = f"**{ty.upper()} Berhasil Membuat String Session** \n\n`{string_session}` \n\n**Support : @amwangs**"
    try:
        if not is_bot:
            await client.send_message("me", text)
        else:
            await bot.send_message(msg.chat.id, text)
    except KeyError:
        pass
    await client.disconnect()
    await asyncio.sleep(1.0)
    await bot.send_message(msg.chat.id, " {} **Berhasil membuat string session\n\nSilahkan periksa pesan tersimpan anda.**".format("telethon" if telethon else "pyrogram"))


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("Membatalkan Proses Pengambilan String!", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("Mau ngapain banh?", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("Membatalkan Proses Pengambilan String!", quote=True)
        return True
    else:
        return False
