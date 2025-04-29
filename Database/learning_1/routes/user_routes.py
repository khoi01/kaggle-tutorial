from quart import Blueprint, request, jsonify
from models.User import User
from db.database import get_db
from sqlalchemy import select, update, delete
from sqlalchemy.exc import NoResultFound

user_bp = Blueprint("user",__name__)

#create
@user_bp.route("/create",methods=["POST"])
async def create_user():
    data = await request.get_json()
    if not data:
        return jsonify({"error": "No JSON body found"}), 400

    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "Missing required fields"}), 400

    async for session in get_db():
        user = User(name=data["name"],email=data["email"])
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return jsonify({"id": user.id, "name": user.name, "email": user.email}),201


# ✅ Read All
@user_bp.route("/all", methods=["GET"])
async def get_users():
    async for session in get_db():
        result = await session.execute(select(User))
        users = result.scalars().all()
        return jsonify([
            {"id": u.id, "name": u.name, "email": u.email}
            for u in users
        ])
# ✅ Delete
@user_bp.route("/delete/<int:user_id>", methods=["DELETE"])
async def delete_user(user_id):
    async for session in get_db():
        stmt = delete(User).where(User.id == user_id)
        result = await session.execute(stmt)
        await session.commit()

        if result.rowcount == 0:
            return jsonify({"error": "User not found"}), 404
        return jsonify({"message": "User deleted ✅"})

# ✅ Update
@user_bp.route("/users/<int:user_id>", methods=["PUT"])
async def update_user(user_id):
    data = await request.get_json()
    async for session in get_db():
        stmt = update(User).where(User.id == user_id).values(
            name=data.get("name"),
            email=data.get("email")
        ).execution_options(synchronize_session="fetch")

        result = await session.execute(stmt)
        await session.commit()

        if result.rowcount == 0:
            return jsonify({"error": "User not found"}), 404
        return jsonify({"message": "User updated ✅"})

     