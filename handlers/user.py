from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

user_router = Router()

@user_router.message(Command("start"))
async def start_cmd(message: Message):
    await message.answer("👋 Добро пожаловать! Здесь вы можете купить виртуальные номера.")

def register_user_handlers(dp):
    dp.include_router(user_router)
