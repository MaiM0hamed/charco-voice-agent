from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

@app.route("/submit-order", methods=["POST"])
def submit_order():
    try:
        data = request.json
        name = data.get("name", "Unknown")
        order_list = data.get("order_list", [])
        order_id = "ORD" + str(hash(name))[:6]
        eta = "30 minutes"

        # Store in JSON
        order = {"order_id": order_id, "name": name, "order_list": order_list, "eta": eta}
        os.makedirs("data", exist_ok=True)
        with open("data/orders.json", "a") as f:
            json.dump(order, f, ensure_ascii=False)
            f.write("\n")

        return jsonify({"order_id": order_id, "eta": eta})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)