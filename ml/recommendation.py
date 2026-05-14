import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# LOAD DATA ONCE
description_df = pd.read_csv(os.path.join(BASE_DIR, "datasets", "description.csv"))
precautions_df = pd.read_csv(os.path.join(BASE_DIR, "datasets", "precautions_df.csv"))
medications_df = pd.read_csv(os.path.join(BASE_DIR, "datasets", "medications.csv"))
diets_df = pd.read_csv(os.path.join(BASE_DIR, "datasets", "diets.csv"))
workout_df = pd.read_csv(os.path.join(BASE_DIR, "datasets", "workout_df.csv"))

# CONVERT TO FAST LOOKUP MAPS
desc_map = dict(zip(description_df["Disease"], description_df["Description"]))

med_map = medications_df.groupby("Disease")["Medication"].apply(list).to_dict()

diet_map = diets_df.groupby("Disease")["Diet"].apply(list).to_dict()

workout_map = workout_df.groupby("disease")["workout"].apply(list).to_dict()

# precautions (multi-column flatten)
precaution_map = {}
for _, row in precautions_df.iterrows():
    disease = row["Disease"]
    vals = row.drop("Disease").dropna().tolist()
    precaution_map[disease] = vals

# MAIN FUNCTION (FAST)
def get_recommendation(disease):

    return {
        "disease": disease,
        "description": desc_map.get(disease, "No description available"),
        "precautions": precaution_map.get(disease, []),
        "medications": med_map.get(disease, []),
        "diet": diet_map.get(disease, []),
        "workout": workout_map.get(disease, [])
    }