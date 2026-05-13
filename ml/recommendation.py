import os
import pickle
import numpy as np
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# load model
model = pickle.load(open("models/svc_model.pkl", "rb"))
# load encoder
le = pickle.load(open("models/label_encoder.pkl", "rb"))

# LOAD DATASETS (recommendation data)
description_df = pd.read_csv(os.path.join(BASE_DIR, "datasets", "description.csv"))
precautions_df = pd.read_csv(os.path.join(BASE_DIR, "datasets", "precautions_df.csv"))
medications_df = pd.read_csv(os.path.join(BASE_DIR, "datasets", "medications.csv"))
diets_df = pd.read_csv(os.path.join(BASE_DIR, "datasets", "diets.csv"))
workout_df = pd.read_csv(os.path.join(BASE_DIR, "datasets", "workout_df.csv"))

# LOAD SYMPTOMS FROM TRAINING DATA
train_df = pd.read_csv(os.path.join(BASE_DIR, "datasets", "Training.csv"))

symptoms = train_df.columns[:-1]
symptoms_dict = {symptom: i for i, symptom in enumerate(symptoms)}

# PREDICTION FUNCTION
def predict_disease(user_symptoms):

    input_vector = np.zeros(len(symptoms_dict))

    for symptom in user_symptoms:
        symptom = symptom.strip().lower()

        if symptom in symptoms_dict:
            input_vector[symptoms_dict[symptom]] = 1

    prediction = model.predict([input_vector])

    return le.inverse_transform(prediction)[0]

# RECOMMENDATION FUNCTION
def get_recommendation(disease):

    desc = description_df[description_df['Disease'] == disease]['Description'].values
    desc = desc[0] if len(desc) > 0 else "No description available"

    precautions = precautions_df[precautions_df['Disease'] == disease].values.tolist()

    medications = medications_df[medications_df['Disease'] == disease]['Medication'].values.tolist()

    diets = diets_df[diets_df['Disease'] == disease]['Diet'].values.tolist()

    workouts = workout_df[workout_df['disease'] == disease]['workout'].values.tolist()

    return {
        "disease": disease,
        "description": desc,
        "precautions": precautions,
        "medications": medications,
        "diet": diets,
        "workout": workouts
    }

# MAIN TEST
if __name__ == "__main__":

    print("Enter symptoms separated by comma:")
    symptoms_input = input().split(",")

    user_symptoms = [s.strip() for s in symptoms_input]

    # step 1: predict disease
    disease = predict_disease(user_symptoms)

    print("\nPredicted Disease:", disease)

    # step 2: get recommendations
    rec = get_recommendation(disease)

    print("\n--- DESCRIPTION ---")
    print(rec["description"])

    print("\n--- PRECAUTIONS ---")
    print(rec["precautions"])

    print("\n--- MEDICATIONS ---")
    print(rec["medications"])

    print("\n--- DIET ---")
    print(rec["diet"])

    print("\n--- WORKOUT ---")
    print(rec["workout"])