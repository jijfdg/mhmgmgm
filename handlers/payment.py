from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

payment_router = Router()

@payment_router.message(Command("balance"))
async def balance_cmd(message: Message):
    await message.answer("💰 Баланс скоро будет доступен...")

def register_payment_handlers(dp):
    dp.include_router(payment_router)
