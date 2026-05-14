#terminal testing


from predict import predict_disease, symptoms_dict
from recommendation import get_recommendation
import re

# CLEAN INPUT TEXT
def normalize(text):
    text = text.lower()
    text = re.sub(r"[^a-z]", " ", text)   # remove _, commas, numbers, etc.
    text = " ".join(text.split())         # remove extra spaces
    return text


# EXTRA STRONG NORMALIZATION (for matching)
def normalize_key(text):
    return re.sub(r"[^a-z]", "", text.lower())  # removes EVERYTHING non-letter


def extract_symptoms(user_input, symptoms_dict):

    user_input_clean = normalize_key(user_input)

    matched = set()

    for symptom in symptoms_dict.keys():

        symptom_clean = normalize_key(symptom)

        # match anywhere in text
        if symptom_clean in user_input_clean:
            matched.add(symptom)

    return list(matched)

# MAIN SYSTEM
def run_system():

    raw_input = input("Enter symptoms: ")

    user_symptoms = extract_symptoms(raw_input, symptoms_dict)  

    print("\nUser Symptoms:", user_symptoms)

    if not user_symptoms:
        print("\n⚠ No symptoms detected")
        return

    disease = predict_disease(user_symptoms)

    print("\nPredicted Disease:", disease)

    result = get_recommendation(disease)

    print("\n--- DESCRIPTION ---")
    print(result["description"])

    print("\n------- PRECAUTIONS ------")
    print(result["precautions"])

    print("\n----- MEDICATIONS -----")
    print(result["medications"])

    print("\n--- DIET ---")
    print(result["diet"])

    print("\n--- WORKOUT ---")
    print(result["workout"])

if __name__ == "__main__":
    run_system()