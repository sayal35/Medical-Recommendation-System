import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def load_and_preprocess_data():

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(BASE_DIR, "datasets", "Training.csv")


    #load dataset
    df = pd.read_csv(file_path)

    #features
    X=df.drop(columns=['prognosis'])

    #target variable
    y=df['prognosis']

    #encode target variable
    le= LabelEncoder()
    Y= le.fit_transform(y)


    #split dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
    
    return X_train, X_test, y_train, y_test, le