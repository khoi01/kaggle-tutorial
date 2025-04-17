from quart import Blueprint, jsonify
from repository.user_repository import UserRepository

user_bp = Blueprint("users",__name__)


@user_bp.route('/users', methods=['GET'])
async def get_users():
    
   users = await UserRepository.users()
   return jsonify({"users":users})
    
