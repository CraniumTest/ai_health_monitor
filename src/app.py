from flask import Flask, jsonify
import random
import datetime

app = Flask(__name__)

# Simulate collecting data from a wearable device
def get_mock_wearable_data():
    return {
        "heart_rate": random.randint(60, 100),
        "steps": random.randint(1000, 15000),
        "sleep_duration": random.uniform(4.0, 8.0)
    }

@app.route('/health_data', methods=['GET'])
def health_data():
    data = get_mock_wearable_data()
    return jsonify(data)

@app.route('/predict_health_risks', methods=['GET'])
def predict_health_risks():
    # Placeholder for machine learning prediction logic
    risk = "low"  # could be computed based on models in real use case
    return jsonify({"health_risk": risk})

if __name__ == '__main__':
    app.run(debug=True)
