import aiohttp
from config import ITPHONE_API_KEY, ITPHONE_API_URL

async def buy_number(service: str, country: int):
    async with aiohttp.ClientSession() as session:
        url = f"{ITPHONE_API_URL}/get_number?token={ITPHONE_API_KEY}&service={service}&country={country}"
        async with session.get(url) as resp:
            return await resp.json()

async def get_code(order_id: str):
    async with aiohttp.ClientSession() as session:
        url = f"{ITPHONE_API_URL}/get_sms?token={ITPHONE_API_KEY}&id={order_id}"
        async with session.get(url) as resp:
            return await resp.json()
