from flask import Flask,jsonify

#build app
app = Flask(__name__)

#root route
@app.route('/')
def index():
    
    return 'Hello from Flask Environment'

@app.route('/health')
def health():
    return jsonify(
        {
            "status":"okey",
            "health":" overything is good!"
        }
    )

# This block ensures the app runs only if executed directly (not imported)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


