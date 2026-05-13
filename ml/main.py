from predict import predict_disease, symptoms_dict
from recommendation import get_recommendation

# CLEAN TEXT NORMALIZATION
def normalize(text):
    return " ".join(text.lower().strip().split())

# SYMPTOM EXTRACTION (FIXED)
def extract_symptoms(user_input):

    user_input = normalize(user_input)

    matched = set()

    for symptom in symptoms_dict.keys():

        phrase = symptom.replace("_", " ")

        # strict phrase match
        if phrase in user_input:
            matched.add(symptom)

    return list(matched)

# MAIN SYSTEM
def run_system():

    raw_input = input("Enter symptoms: ")

    user_symptoms = extract_symptoms(raw_input)

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