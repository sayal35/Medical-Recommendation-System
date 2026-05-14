from flask import Flask, request, jsonify
from flask_cors import CORS

from predict import predict_disease, symptoms_dict
from recommendation import get_recommendation

import re

app = Flask(__name__)
CORS(app)

# TEXT NORMALIZATION
def normalize_key(text):
    return re.sub(r"[^a-z]", "", text.lower())

# EXTRACT SYMPTOMS
def extract_symptoms(user_input, symptoms_dict):

    user_input_clean = normalize_key(user_input)

    matched = set()

    for symptom in symptoms_dict.keys():

        symptom_clean = normalize_key(symptom)

        if symptom_clean in user_input_clean:
            matched.add(symptom)

    return list(matched)

# HOME ROUTE

@app.route('/')
def home():
    return "Medical Recommendation System API Running"

# PREDICT ROUTE

@app.route('/predict', methods=['POST'])
def predict():

    try:

        data = request.json

        user_input = data.get("symptoms", "")

        # extract symptoms
        user_symptoms = extract_symptoms(
            user_input,
            symptoms_dict
        )

        # no symptoms found
        if not user_symptoms:
            return jsonify({
                "success": False,
                "message": "No symptoms detected"
            })

        # predict disease
        disease = predict_disease(user_symptoms)

        # get recommendations
        result = get_recommendation(disease)

        return jsonify({
            "success": True,
            "detected_symptoms": user_symptoms,
            "disease": result["disease"],
            "description": result["description"],
            "precautions": result["precautions"],
            "medications": result["medications"],
            "diet": result["diet"],
            "workout": result["workout"]
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        })

#symptoms list
@app.route('/symptoms',methods=['GET'])
def get_symptoms():
    return jsonify(list(symptoms_dict.keys()))

# RUN SERVER

if __name__ == "__main__":
    app.run(debug=True)