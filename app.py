from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello from Docker! 🐳</h1><p>My first containerized Python app.</p>"

@app.route("/api/health")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))