import os
from dotenv import load_dotenv

load_dotenv()

def get_env_var(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise ValueError(f"[❌] Переменная окружения '{name}' не задана!")
    return value

BOT_TOKEN = get_env_var("8430063928:AAFidIFAxHZ9zxOpB6I6xHU99-Zt1YZ6zz4")
ITPHONE_API_KEY = get_env_var("435520:AAtK4zW54f8Oueygnfm1vyHYLFat1CgFGsc")
CRYPTOBOT_TOKEN = get_env_var("435520:AAtK4zW54f8Oueygnfm1vyHYLFat1CgFGsc")

# API URLs
ITPHONE_API_URL = "https://api.itphone.app"
CRYPTOBOT_API_URL = "https://pay.crypt.bot/api"
