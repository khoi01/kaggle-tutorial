from quart import Blueprint,request,jsonify,current_app
import os
import asyncio


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
    asyncio.create_task( AIModelService.analyze_and_log()
    )
    return jsonify({
            "success": True,
            "message": "Image received. Processing in background."
        })
