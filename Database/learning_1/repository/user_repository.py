from models.User import User
from sqlalchemy import select,update,delete

class UserRepository:
    @staticmethod
    async def get_all(session):
        result = await session.execute(select(User))
        return result.scalars().all()