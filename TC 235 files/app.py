from flask import Flask, request
import json
import pickle
import numpy as np

SAVED_MODEL_PATH = "regression_model.pkl"
regression_model = pickle.load(open(SAVED_MODEL_PATH, "rb"))

app = Flask(__name__)

def process_data(data: list) -> np.array:
    np_array = np.asarray(data)
    if np_array.ndim == 1:
        np_array = [np_array]
    return np_array

@app.route('/price', methods=["POST"])
def price_predict() -> str:
    if request.method == "POST":
        try:
            features = process_data(json.loads(request.data))
            predictions = regression_model.predict(features)
            return json.dumps({'predicted': predictions.tolist()}), 200
        except:
            return json.dumps({"error": "INPUT MUST BE A 2D ARRAY"}), 400

    else:
        return json.dumps({"error": "METHOD NOT ALLOWED"}), 405

if __name__ == "__main__":
    app.run(debug=True)