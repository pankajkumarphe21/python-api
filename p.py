from flask import Flask, jsonify, request
from flask_cors import CORS
import pickle
import numpy as np
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": os.getenv('BACKEND_URL')}})

with open("linear_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to Vercel Deployed API!"})

@app.route("/user/<userId>")
def getUser(userId):
    return jsonify(f"Hi {userId}")

@app.route("/predict/<input>",methods=['POST'])
def predict(input):
    data = [int(input)]
    inputs = np.array(data).reshape(1,-1)
    predictions = model.predict(inputs).tolist()
    return jsonify({"predictions": predictions})


if __name__ == "__main__":
    app.run(port=5000)