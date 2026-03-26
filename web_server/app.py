from flask import Flask, render_template, jsonify, request
import threading

app = Flask(__name__)

stats_data = {"cpu": 0, "ram": 0}
stats_lock = threading.Lock()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/stats", methods=["GET", "POST"])
def stats():
    global stats_data

    if request.method == "POST":
        data = request.get_json()
        with stats_lock:
            stats_data["cpu"] = data.get("cpu", 0)
            stats_data["ram"] = data.get("ram", 0)
        return jsonify({"status": "ok"})

    with stats_lock:
        return jsonify({"cpu": stats_data["cpu"], "ram": stats_data["ram"]})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
