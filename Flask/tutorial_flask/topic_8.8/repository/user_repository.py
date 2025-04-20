import asyncio
from quart import current_app

class UserRepository:
    users_data = [
    {"id": 1, "name": "Ali"},
    {"id": 2, "name": "Fatimah"},
    {"id": 3, "name": "John"}
    ]
    
    @classmethod
    async def users(cls):
        app = current_app._get_current_object()
        await asyncio.sleep(1)  # Simulate delay
        return cls.users_data

