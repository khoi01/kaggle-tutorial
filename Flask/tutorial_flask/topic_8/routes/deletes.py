import os


from flask import Blueprint,request, jsonify , current_app

deletes_bp = Blueprint("deletes",__name__)

#DELETE
@deletes_bp.route("/delete/<item>",methods=["DELETE"])
def delete_item(item):
    return jsonify({
        "item_deleted": item,
        "status": "Deleted"
    })