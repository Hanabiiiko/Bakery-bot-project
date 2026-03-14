# 🍰 Telegram-бот кондитерской "Светлана"

[![Maintainability](https://qlty.sh/gh/Hanabiiiko/projects/backend-project-44/maintainability.svg)](https://qlty.sh/gh/Hanabiiiko/projects/backend-project-44)

## Описание
Telegram-бот для автоматизации приема заказов домашней кондитерской. Приложение собирает заявки от клиентов (выбор категории товара, пожелания по оформлению, удобное время для связи и дедлайн)

## Стек технологий
* **Язык:** Python 3.10+
* **Фреймворк:** aiogram 3.x
* **База данных:** SQLite + aiosqlite
* **Конфигурация:** python-dotenv

## Демонстрация
* **Демонстрация работы (Видео):** 

## Инструкция по запуску (Локально)

1. **Клонируйте репозиторий:**
   ```bash
   git clone [https://github.com/Hanabiiiko/Bakery-tg-bot.git](https://github.com/Hanabiiiko/Bakery-tg-bot.git)
   cd Bakery-tg-bot

2. **Создайте и активируйте виртуальное окружение:**

Bash
python -m venv venv
# Для Windows:
venv\Scripts\activate
# Для macOS/Linux:
source venv/bin/activate

3. **Установите зависимости:**

Bash
pip install -r requirements.txt

4. **Настройте переменные окружения:**
Создайте файл .env в корневой папке проекта и добавьте ваши конфиденциальные данные:

Code snippet
BOT_TOKEN=ваш_токен_от_BotFather
BAKER_ID=ваш_telegram_id

5. **Запустите бота:**

Bash
python main.py
