import pickle
import threading
import json

from flask import Flask, request
from werkzeug import serving
import numpy as np

SAVED_MODEL_PATH = "svm_model.pkl"

svm = pickle.load(open(SAVED_MODEL_PATH, "rb"))

app = Flask(__name__)

def __process_input(request_data: str) -> np.array:
    parsed_body = np.asarray(json.loads(request_data)["inputs"])
    n = len(parsed_body)
    parsed_body = parsed_body.reshape((n, -1))
    return parsed_body

@app.route("/predict", methods=["POST"])
def predict() -> str:
    try:
        input_params = __process_input(request.data)
        predictions = svm.predict(input_params)

        return json.dumps({"predicted_class": predictions.tolist()})
    except (KeyError, json.JSONDecodeError, AssertionError):
        return json.dumps({"error": "CHECK INPUT"}), 400
    except:
        return json.dumps({"error": "PREDICTION FAILED"}), 500