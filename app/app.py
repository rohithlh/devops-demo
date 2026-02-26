from flask import Flask, jsonify
import os
import socket
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to DevOps Demo App!",
        "hostname": socket.gethostname(),
        "environment": os.getenv("APP_ENV", "development"),
        "version": "1.0.0",
        "timestamp": datetime.datetime.utcnow().isoformat()
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/ready")
def ready():
    return jsonify({"status": "ready"}), 200

@app.route("/info")
def info():
    return jsonify({
        "app": "devops-demo",
        "version": "1.0.0",
        "author": "DevOps Learner",
        "description": "A demo app to practice full DevOps pipeline"
    })

@app.route("/metrics-demo")
def metrics_demo():
    return jsonify({"requests_total": 42, "uptime_seconds": 3600})

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
