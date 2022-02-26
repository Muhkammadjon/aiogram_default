from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inlinekeyboardbuttons.callback_datas.callback import course_callback, course_sing

cancelbutton = InlineKeyboardButton(text="back", callback_data=callback.new("back"))

inlinebutton = InlineKeyboardButton(text="*", callback_data=callback.new(course_name="******"))
inlinebuttonpack = InlineKeyboardMarkup(row_width=1).add(inlinebutton)
