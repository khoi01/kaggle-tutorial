from quart import Blueprint,request,jsonify,current_app
import os


from services.ai_model_service import AIModelService

ai_bp = Blueprint("ai_bp",__name__)


@ai_bp.route('/detect', methods=['GET'])
async def detect():
    # files = await request.files
    # if "image" not in files:
    #     return jsonify({"success": False, "message": "No file uploaded"}), 400

    # image = files["image"]

    # # Save file
    # upload_dir = current_app.config.get("UPLOAD_DIR", "uploads")
    # os.makedirs(upload_dir, exist_ok=True)

    # save_path = os.path.join(upload_dir, image.filename)
    # await image.save(save_path)

    # Simulate AI processing
    result = await AIModelService.analyze_image()
    
    return jsonify({
    "success": True,
    "prediction": result
    })
