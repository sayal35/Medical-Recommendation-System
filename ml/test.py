from predict import predict_disease
from preprocess import load_and_preprocess_data

X_train, X_test, y_train, y_test, le = load_and_preprocess_data()

# test samples
print("Pred:", predict_disease(X_test.iloc[0].values))
print("Actual:", le.inverse_transform([y_test[0]]))

print("Pred:", predict_disease(X_test.iloc[10].values))
print("Actual:", le.inverse_transform([y_test[10]]))