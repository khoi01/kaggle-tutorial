from flask import Blueprint, jsonify

basic_bp = Blueprint('basic', __name__)

@basic_bp.route("/hello", methods=["GET"])
def hello_world():
    return jsonify({"message": "Hello from Flask Modular Route!"})

@basic_bp.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "API is running"})
