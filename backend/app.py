from flask import Flask, request, jsonify
import pickle
import numpy as np
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

model = pickle.load(open("../model/model.pkl","rb"))

client = MongoClient("mongodb://localhost:27017/")
db = client["houseDB"]
collection = db["predictions"]

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    area = data["area"]
    bedrooms = data["bedrooms"]
    age = data["age"]

    prediction = model.predict([[area,bedrooms,age]])

    result = float(prediction[0])

    collection.insert_one({
        "area": area,
        "bedrooms": bedrooms,
        "age": age,
        "predicted_price": result
    })

    return jsonify({"predicted_price": result})


if __name__ == "__main__":
    app.run(debug=True)