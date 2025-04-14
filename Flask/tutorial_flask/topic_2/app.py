# app.py

from flask import Flask, request, jsonify

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
