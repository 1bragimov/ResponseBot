import asyncio
import logging
import sys
from os import getenv
from aiogram import Bot, Dispatcher, F
from aiogram.client import bot
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, BotCommand
from root import TOKEN
from button import uzboard


logging.basicConfig(level=logging.INFO)


dp = Dispatcher()

########################################################

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hurmatli foydalavuvchi {message.from_user.first_name} siz Response_bot🤖ni ishga⚙️ tushirdingiz😎", reply_markup=uzboard)


# @dp.message()
# async def echo(message: Message):
#     await message.reply(message.text)


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
