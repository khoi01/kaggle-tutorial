from quart import Blueprint, jsonify
from sqlalchemy import text
from database.db import Database

health_bp = Blueprint("health_bp", __name__)

@health_bp.route("/ping-db")
async def ping_db():
    try:
        engine = Database.get_engine()
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))  # ✅ Properly wrapped
        return jsonify({
            "status": "success",
            "message": "Database is alive!"
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
