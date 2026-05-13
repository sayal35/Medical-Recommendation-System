import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# load datasets
description_df = pd.read_csv(os.path.join(BASE_DIR, "datasets", "description.csv"))
precautions_df = pd.read_csv(os.path.join(BASE_DIR, "datasets", "precautions_df.csv"))
medications_df = pd.read_csv(os.path.join(BASE_DIR, "datasets", "medications.csv"))
diets_df = pd.read_csv(os.path.join(BASE_DIR, "datasets", "diets.csv"))
workout_df = pd.read_csv(os.path.join(BASE_DIR, "datasets", "workout_df.csv"))


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
