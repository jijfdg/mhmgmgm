import aiohttp
from config import CRYPTOBOT_TOKEN, CRYPTOBOT_API_URL

async def create_invoice(amount: float, currency: str, user_id: int):
    url = f"{CRYPTOBOT_API_URL}/createInvoice"
    headers = {"Crypto-Pay-API-Token": CRYPTOBOT_TOKEN}
    data = {
        "asset": currency,
        "amount": amount,
        "description": "Покупка номера",
        "hidden_message": str(user_id)
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as resp:
            return await resp.json()
