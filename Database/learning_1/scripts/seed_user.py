import asyncio
from db.database import get_db
from models.User import User

dummy_users = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
    {"name": "Charlie", "email": "charlie@example.com"},
    {"name": "Dana", "email": "dana@example.com"},
]

async def seed_users():
    async for session in get_db():
        print("🌱 Seeding users...")
        for user in dummy_users:
            session.add(User(name=user["name"], email=user["email"]))
        await session.commit()
        print("✅ Users seeded successfully.")
        break  # Prevents multiple sessions

if __name__ == "__main__":
    asyncio.run(seed_users())
