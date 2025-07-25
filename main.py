from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
import asyncio
import logging

from config import BOT_TOKEN
from handlers.user import register_user_handlers
from handlers.payment import register_payment_handlers
from utils.scheduler import start_scheduler
from database.db import init_db

logging.basicConfig(level=logging.INFO)

async def main():
    await init_db()
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    register_user_handlers(dp)
    register_payment_handlers(dp)

    await start_scheduler(bot)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
