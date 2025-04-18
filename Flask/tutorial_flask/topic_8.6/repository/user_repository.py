import asyncio

class UserRepository:
    users_data = [
    {"id": 1, "name": "Ali"},
    {"id": 2, "name": "Fatimah"},
    {"id": 3, "name": "John"}
    ]
    
    @staticmethod
    async def users():
        await asyncio.sleep(1)  # Simulate delay
        return UserRepository.users_data

