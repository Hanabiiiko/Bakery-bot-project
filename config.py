import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("Error: BOT_TOKEN не найден в .env")


baker_id_str = os.getenv("BAKER_ID")
if not baker_id_str:
    raise ValueError("Error: BAKER_ID не найден в .env")
BAKER_ID = int(baker_id_str)

DB_PATH = "bakery_orders.db"
