import os
from dotenv import load_dotenv

load_dotenv()

def get_env_var(name: str) -> str:
    value = os.getenv(name)
    print(f"[DEBUG] {name} =", value)  # Выводим переменные окружения
    if not value:
        raise ValueError(f"[❌] Переменная окружения '{name}' не задана!")
    return value

BOT_TOKEN = get_env_var("BOT_TOKEN")
ITPHONE_API_KEY = get_env_var("ITPHONE_API_KEY")
CRYPTOBOT_TOKEN = get_env_var("CRYPTOBOT_TOKEN")

ITPHONE_API_URL = "https://api.itphone.app"
CRYPTOBOT_API_URL = "https://pay.crypt.bot/api"
