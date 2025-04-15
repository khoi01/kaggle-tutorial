# app.py
import os

from flask import Flask, request, jsonify
from dotenv import load_dotenv

#Load variables from .env file
load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["UPLOAD_DIR"] = os.getenv("UPLOAD_DIR","uploads") #default
#Folder where its store images
UPLOAD_FOLDER = "uploads"
#Create new direcotry if not existed
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


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
      
#JSON EXAMPLE (POST)
@app.route('/json', methods=['POST'])
def json_input():
    data = request.get_json()
    name = data.get("name","Anonymous") #default value: Anonymous
    return jsonify({
        "success": True,
        "message": f"Hello, {name}!",
        "code":200
    })
    

#FORM DATA (POST)EXAMPLE:LOGIN,SuBMIT,etc
@app.route('/form', methods=['POST'])
def form_input():
    name = request.form.get("name","no name")
    age = request.form.get("age","unknown")
    return jsonify({
        "success": True,
        "name": name,
        "age": age
    })
# File upload
@app.route("/upload", methods=["POST"])
def upload_file():
    if "image" not in request.files:
        return jsonify({"success": False, "message": "No file part"}), 400

    file = request.files["image"]
    if file.filename == "":
        return jsonify({"success": False, "message": "No selected file"}), 400

    # Save the file to uploads
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    
    # For now, just return filename (we’ll save it later)
    return jsonify({"success": True, "filename": file.filename})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
