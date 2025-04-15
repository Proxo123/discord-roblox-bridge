import os
from flask import Flask, request, jsonify
from gevent.pywsgi import WSGIServer  # Production server

app = Flask(__name__)

@app.route('/print', methods=['POST'])
def handle_print():
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({"error": "Missing 'message' field"}), 400
            
        print(f"[Roblox]: {data['message']}")  # Will appear in Railway logs
        return jsonify({"status": "success"}), 200
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

def run_production():
    port = int(os.getenv('PORT', 5000))
    http_server = WSGIServer(('0.0.0.0', port), app)
    print(f"Production server running on port {port}")
    http_server.serve_forever()

if __name__ == '__main__':
    if os.getenv('RAILWAY_ENVIRONMENT'):  # Detect if running on Railway
        run_production()
    else:
        print("Dev server running on port 5000")
        app.run(host='0.0.0.0', port=5000, debug=True)
