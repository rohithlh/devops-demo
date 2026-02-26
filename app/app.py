
@app.route("/metrics-demo")
def metrics_demo():
    return jsonify({"requests_total": 42, "uptime_seconds": 3600})
