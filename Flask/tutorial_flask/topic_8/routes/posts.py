import os


from flask import Blueprint,request, jsonify , current_app

posts_bp = Blueprint("posts",__name__)



#JSON EXAMPLE (POST)
@posts_bp.route('/json', methods=['POST'])
def json_input():
    data = request.get_json()
    name = data.get("name","Anonymous") #default value: Anonymous
    return jsonify({
        "success": True,
        "message": f"Hello, {name}!",
        "code":200
    })
    

#FORM DATA (POST)EXAMPLE:LOGIN,SuBMIT,etc
@posts_bp.route('/form', methods=['POST'])
def form_input():
    name = request.form.get("name","no name")
    age = request.form.get("age","unknown")
    return jsonify({
        "success": True,
        "name": name,
        "age": age
    })
# File upload
@posts_bp.route("/upload", methods=["POST"])
def upload_file():
    
        #Create new direcotry if not existed
    os.makedirs(current_app.config["UPLOAD_DIR"]
    , exist_ok=True)
    
    if "image" not in request.files:
        return jsonify({"success": False, "message": "No file part"}), 400

    file = request.files["image"]
    if file.filename == "":
        return jsonify({"success": False, "message": "No selected file"}), 400

    # Save the file to uploads
    filepath = os.path.join( current_app.config["UPLOAD_DIR"]
, file.filename)
    file.save(filepath)
    
    # For now, just return filename (we’ll save it later)
    return jsonify({"success": True, "filename": file.filename})
