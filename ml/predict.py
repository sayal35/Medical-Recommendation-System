import os
import pickle
import numpy as np
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_DIR = os.path.join(BASE_DIR, "models")  

model = pickle.load(open(os.path.join(MODEL_DIR, "svc_model.pkl"), "rb"))
le = pickle.load(open(os.path.join(MODEL_DIR, "label_encoder.pkl"), "rb"))

# load training data to get feature order
train_df = pd.read_csv(os.path.join(BASE_DIR, "datasets", "Training.csv"))

symptoms = train_df.columns[:-1]
symptoms_dict = {symptom: i for i, symptom in enumerate(symptoms)}


def predict_disease(user_symptoms):

    input_vector = np.zeros(len(symptoms_dict))

    for symptom in user_symptoms:
        symptom = symptom.strip().lower()

        if symptom in symptoms_dict:
            input_vector[symptoms_dict[symptom]] = 1


    prediction = model.predict([input_vector])

    return le.inverse_transform(prediction)[0]

