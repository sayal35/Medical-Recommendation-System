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

#create models folder 
os.makedirs("models", exist_ok=True)

#save model
pickle.dump(svc, open("models/svc_model.pkl", "wb"))

#save label encoder
pickle.dump(le, open("models/label_encoder.pkl", "wb"))
