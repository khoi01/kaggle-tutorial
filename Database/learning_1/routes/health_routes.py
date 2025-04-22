from quart import Blueprint,jsonify
from sqlalchemy import text #need for raw SQL
from db.database import engine 


health_bp = Blueprint("health",__name__)

@health_bp.route("/ping-db")
async def ping_db():
    try:
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        return jsonify({
            "status": "success",
            "message": "Database is alive ✅"
})
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }),50
