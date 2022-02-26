import logging

# from aiogram.utils.executor import start_webhook
from aiogram.utils.executor import start_polling
from aiogram.types.bot_command import BotCommand
import middlewares, handlers
from data.config import ADMIN_ID, WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT
from loader import dp

logging.basicConfig(level=logging.INFO)


async def on_startup(dispatcher):
    middleware = middlewares
    handler = handlers
    command = [
        BotCommand("/start", "start")
    ]
    await dp.bot.set_my_commands(commands=command)

    await dp.bot.send_message(ADMIN_ID, text="the bot is working")
#     await dp.bot.set_webhook(WEBHOOK_URL)

async def on_shutdown(dp):
    logging.warning('Shutting down..')
    await dp.bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()
    logging.warning('Bye!')


if __name__ == '__main__':
    start_polling(dp, on_startup=on_startup, skip_updates=True)
#     start_webhook(
#         dispatcher=dp,
#         webhook_path=WEBHOOK_PATH,
#         on_startup=on_startup,
#         on_shutdown=on_shutdown,
#         skip_updates=True,
#         host=WEBAPP_HOST,
#         port=WEBAPP_PORT,
#     )
