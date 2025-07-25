# Telegram Бот для продажи номеров через Itphone с оплатой через CryptoBot

## 🚀 Установка

1. Установите зависимости:
```bash
pip install -r requirements.txt
```

2. Создайте файл `.env` на основе `.env.example`.

3. Запустите бота:
```bash
python main.py
```

## ⚙️ Переменные окружения

- `BOT_TOKEN` — токен Telegram-бота
- `ITPHONE_API_KEY` — API ключ от Itphone
- `CRYPTOBOT_TOKEN` — токен от CryptoBot

## 🛠 Используемые технологии

- aiogram
- aiohttp
- aiosqlite
- apscheduler
