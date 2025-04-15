# app.py
import os

from flask import Flask, request, jsonify
from dotenv import load_dotenv
from routes.posts import posts_bp
from routes.gets import gets_bp
from routes.deletes import deletes_bp

#Load variables from .env file
load_dotenv()

def create_app():
    

    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["UPLOAD_DIR"] = os.getenv("UPLOAD_DIR","uploads") #default

    app.register_blueprint(posts_bp,url_prefix="/posts")
    app.register_blueprint(gets_bp,url_prefix="/gets")
    app.register_blueprint(deletes_bp,url_prefix="/deletes")

        
    return app
      

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host='0.0.0.0')
