import logging

import wikipedia
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '2060379086:AAFrpVCSzujFC_TUILxNkIrR1rAx6OV4exs'
wikipedia.set_lang('uz')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalomu Alaykum!\nWikipedia botiga xush kelibsiz.\nIzlayotgan ma'lumotingizni kiriting.")


@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga doir ma'qola topilmadi.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
