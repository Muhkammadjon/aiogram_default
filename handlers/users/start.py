import sqlite3

from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMIN_ID
from keyboards.keyboardbuttons import keyboardbutton
from loader import bot, dp, db
from states.state import CoderBot
from utils.misc import rate_limit


@rate_limit(limit=10)
@dp.message_handler(commands="start")
async def send_welcome(message: types.Message):
    try:
        db.add_user(id=message.chat.id, allname=message.from_user.first_name)
    except sqlite3.IntegrityError:
        pass
    await bot.send_message(chat_id=message.from_user.id, text="<s>Welcome</s> to <s>anonymous chat</s>",
                           parse_mode=types.ParseMode.HTML)
    await message.answer(
        f"""Привет {message.from_user.first_name}, Эта бот """,
        parse_mode="HTML")
