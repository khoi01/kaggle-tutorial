import os
import asyncio

from quart import Blueprint,request, jsonify , current_app

gets_bp = Blueprint("gets",__name__)

    #GET
@gets_bp.route('/config')
def show_config():
    return{
        "env": current_app.config["SECRET_KEY"] ,
        "upload_dir":current_app.config["UPLOAD_DIR"] 
    }
    
#GET
@gets_bp.route('/status')
def status():
    response = {
        "code":200,
        "success": True,
        "message": "API is working",
        "data": None
    }
    #return jsonify(response)
    return response

#GET
@gets_bp.route("/")
def home():
    return "Hello, Flask from Docker! 🚀"
    
#GET
@gets_bp.route("/greet")
def greet():
    name = request.args.get("name","Guest")
    return f"Hello, {name}!"

#GET
@gets_bp.route("/message")
async def message():
    data =  await request.get_json()
    return jsonify({
        "received": data,
        "status": "message received."
    })
