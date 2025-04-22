from quart import Quart, jsonify
from dotenv import load_dotenv
import os
from routes.health_routes import health_bp
load_dotenv()

def create_app():
    app = Quart(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["UPLOAD_DIR"] = os.getenv("UPLOAD_DIR", "uploads")
    
    #register blueprint
    app.register_blueprint(health_bp,url_prefix="/health")
    return app

app = create_app()

@app.route("/")
async def index():
    return jsonify({"message": "Quart API is live 🚀"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
