import aiosqlite
from config import DB_PATH

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                category TEXT,
                comment TEXT,
                contact_time TEXT,
                deadline TEXT
            )
        ''')
        await db.commit()

async def save_order(username: str, category: str, comment: str, contact_time: str, deadline: str) -> int:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute('''
            INSERT INTO orders (username, category, comment, contact_time, deadline)
            VALUES (?, ?, ?, ?, ?)
        ''', (username, category, comment, contact_time, deadline))
        await db.commit()
        return cursor.lastrowid
