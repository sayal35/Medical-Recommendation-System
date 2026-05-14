from preprocess import load_and_preprocess_data

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix
import pickle
import os

#get preprocessed data

X_train, X_test, y_train, y_test, le = load_and_preprocess_data()

#create model
svc= SVC(kernel='linear', random_state=42)

#train model
svc.fit(X_train, y_train)

#make predictions
y_pred= svc.predict(X_test)

#evaluate model's accuracy
accuracy= accuracy_score(y_test, y_pred)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "models")

os.makedirs(MODEL_DIR, exist_ok=True)

pickle.dump(svc, open(os.path.join(MODEL_DIR, "svc_model.pkl"), "wb"))
pickle.dump(le, open(os.path.join(MODEL_DIR, "label_encoder.pkl"), "wb"))
