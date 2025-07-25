from apscheduler.schedulers.asyncio import AsyncIOScheduler
from services.itphone_api import get_code

async def check_codes():
    # Здесь должна быть логика проверки заказов и получения кодов
    pass

async def start_scheduler(bot):
    scheduler = AsyncIOScheduler()
    scheduler.add_job(check_codes, "interval", seconds=20)
    scheduler.start()
