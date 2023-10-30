from pyrogram.types import Message
from pyrogram import Client, filters
from config import *
from .database.user import add_served_user, get_served_users
import os
import sys
import asyncio


@Client.on_message(filters.private & ~filters.service, group=1)
async def users_sql(_, msg: Message):
    await add_served_user(msg.from_user.id)


@Client.on_message(filters.user(OWNER_ID) & filters.command("stats"))
async def _stats(_, msg: Message):
    users = len(await get_served_users())
    await msg.reply_text(f"**✓ Kumpulan babi babi liar :\n\nTotal ada `{users}` babi **")


@Client.on_message(filters.command("bacot"))
async def _bacot(bot: Client, message: Message):
    if message.from_user.id == OWNER_ID:
        return await message.reply_text(
            "<b>LU SIAPA MONYED, BABI, BANGSAT, KONTOL, MMK, PELER KUDA, SEMPAK KADAL, KANCUT FIR'AUN,DAKI GORILA, UPIL JERAPA, JEMBUD SINGA, TOPENG MONYET, SOFTEX KUNTILANAK, KOLOR POCONG, POPOK TUYUL, JIGONG GENDERUWO.</b>"
        )
    if len(message.command) > 1:
        text = " ".join(message.command[1:])
    elif message.reply_to_message is not None:
        text = message.reply_to_message.text
    else:
        return await message.reply(
            "<code>Silakan sertakan pesan atau balas pesan yang ingin disiarkan.</code>"
        )
      
    kntl = 0
    mmk = []
    jmbt = len(await get_served_users())
    babi = await get_served_users()
    for x in babi:
            mmk.append(int(x["user_id"]))
    for i in mmk:
        try:
            await bot.send_message(i, text)
            kntl += 1
        except Exception as e:
            await message.reply(f"**Error saat mengirim pesan ke `{x}` babi, Karena: `{e}`**")
    return await message.reply(f"**Berhasil memotong {kntl} babi, dari `{jmbt}` babi.**")
    
    
@Client.on_message(filters.command("gas"))
async def _gas(bot: Client, message: Message):
    if message.from_user.id == OWNER_ID:
        return await message.reply_text(
            "<b>LU SIAPA MONYED, BABI, BANGSAT, KONTOL, MMK, PELER KUDA, SEMPAK KADAL, KANCUT FIR'AUN,DAKI GORILA, UPIL JERAPA, JEMBUD SINGA, TOPENG MONYET, SOFTEX KUNTILANAK, KOLOR POCONG, POPOK TUYUL, JIGONG GENDERUWO.</b>"
        )
    else:
        try:
            ajg = await message.reply_text("**Bentar bang...**")
            await asyncio.sleep(2)
            await ajg.delete()
            await message.reply_text("✅ <b>Aku Berhasil Di Update.</b>")
            os.execvp(sys.executable, [sys.executable, "bot.py"])
        except Exception as e:
            print(e)
