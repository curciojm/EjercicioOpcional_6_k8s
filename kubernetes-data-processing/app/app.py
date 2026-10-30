from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
DB_ENDPOINT = os.getenv("DB_ENDPOINT", "localhost")


@app.route("/")
def home():
    return jsonify({
        "application": "Data Processing Service",
        "hostname": socket.gethostname(),
        "log_level": LOG_LEVEL,
        "db_endpoint": DB_ENDPOINT,
        "version": "2.0"
    })


@app.route("/healthz")
def health():
    return jsonify({"status": "alive"}), 200


@app.route("/readyz")
def readiness():
    return jsonify({"status": "ready"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)