# app.py
import os

from flask import Flask, request, jsonify
from dotenv import load_dotenv


#Load variables from .env file
load_dotenv()

def create_app():
    

    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["UPLOAD_DIR"] = os.getenv("UPLOAD_DIR","uploads") #default

    from routes.posts import posts_bp
    app.register_blueprint(posts_bp,url_prefix="/posts")

    #GET
    @app.route('/config')
    def show_config():
        return{
            "env": app.config["SECRET_KEY"] ,
            "upload_dir":app.config["UPLOAD_DIR"] 
        }
    #GET
    @app.route('/status')
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
    @app.route("/")
    def home():
        return "Hello, Flask from Docker! 🚀"
        
    #GET
    @app.route("/greet")
    def greet():
        name = request.args.get("name","Guest")
        return f"Hello, {name}!"

    #POST
    @app.route("/message",methods=["POST"])
    def message():
        data = request.get_json()
        return jsonify({
            "received": data,
            "status": "message received."
        })

    #DELETE
    @app.route("/delete/<item>",methods=["DELETE"])
    def delete_item(item):
        return jsonify({
            "item_deleted": item,
            "status": "Deleted 🗑️"
        })
        
    return app
      

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host='0.0.0.0')
