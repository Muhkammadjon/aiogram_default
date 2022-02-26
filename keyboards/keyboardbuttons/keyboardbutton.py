from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button = KeyboardButton("✔")

buttonpack = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button)
