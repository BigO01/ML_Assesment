import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd


iris_df = pd.read_csv('Iris.csv')
X = iris_df.drop('Species', axis=1)
y = iris_df['Species']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


classifiers = {
    'knn': None,
    'randomforest': None,
    'svm': None,
    'logisticregression': None
}


def load_models():
    models = {}
    for classifier_name in classifiers.keys():
        if classifier_name == 'knn':
            models[classifier_name] = KNeighborsClassifier(n_neighbors=3)
        elif classifier_name == 'randomforest':
            models[classifier_name] = RandomForestClassifier(n_estimators=100, random_state=42)
        elif classifier_name == 'svm':
            models[classifier_name] = SVC(kernel='linear', random_state=42)
        elif classifier_name == 'logisticregression':
            models[classifier_name] = LogisticRegression(multi_class='ovr', random_state=42)

        models[classifier_name].fit(X_train, y_train)

    return models


models = load_models()


def predict_with_model(classifier_name, target):
    if classifier_name not in classifiers:
        return {"error": "Invalid classifier"}

    input_data = np.array([list(map(float, target.split(',')))])
    prediction = models[classifier_name].predict(input_data)

    return prediction[0]
