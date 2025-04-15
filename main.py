from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/print', methods=['POST'])
def handle_print():
    data = request.json
    print(f"[Roblox]: {data['message']}")
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
