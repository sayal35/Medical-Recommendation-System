import pickle
import numpy as np
from preprocess import load_and_preprocess_data

# load model
model = pickle.load(open("models/svc_model.pkl", "rb"))

# load encoder
le = pickle.load(open("models/label_encoder.pkl", "rb"))

# load only symptoms structure (optional)
X_train, X_test, y_train, y_test, _ = load_and_preprocess_data()


def predict_disease(input_data):

    input_array = np.array(input_data).reshape(1, -1)

    prediction = model.predict(input_array)

    return le.inverse_transform(prediction)[0]