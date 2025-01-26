import asyncpg
from .db_config import DATABASE_URL

async def save_user_phone(user_id, phone_number):
    conn = await asyncpg.connect(DATABASE_URL)
    await conn.execute("""
        INSERT INTO users (user_id, phone_number) VALUES ($1, $2)
        ON CONFLICT (user_id) DO NOTHING
    """, user_id, phone_number)
    await conn.close()
