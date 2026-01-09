from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

@app.route("/")
def home():
    return send_file("index.html")

@app.route("/api/convert", methods=["GET"])
def convert():
    """
    Example: /api/convert?value=5&from=feet&to=inches
    """
    try:
        value = float(request.args.get("value", 0))
        from_unit = request.args.get("from")
        to_unit = request.args.get("to")
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid value"}), 400

    if from_unit is None or to_unit is None:
        return jsonify({"error": "Please provide 'from' and 'to' units"}), 400

    # Simple example conversions
    if from_unit == "feet" and to_unit == "inches":
        result = value * 12
    elif from_unit == "inches" and to_unit == "feet":
        result = value / 12
    elif from_unit == "celsius" and to_unit == "fahrenheit":
        result = (value * 9/5) + 32
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        result = (value - 32) * 5/9
    elif from_unit == "centimeters" and to_unit == "inches":
        result = value / 2.54
    elif from_unit == "inches" and to_unit == "centimeters":
        result = value * 2.54
    elif from_unit == "feet" and to_unit == "centimeters":
        result = value * 30.48
    elif from_unit == "centimeters" and to_unit == "feet":
        result = value / 30.48

    else:
        return jsonify({"error": "Conversion not supported yet"}), 400

    return jsonify({
        "input": {
            "value": value,
            "from": from_unit,
            "to": to_unit
        },
        "output": result
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)
