import pandas as pd
data = pd.read_csv(r"student-por.csv") # Training Set
testData = pd.read_csv(r"student-mat.csv") # Testing Set

# Label Encoded catergorical data
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
X_train = data.iloc[:, 0:32]
X_train = X_train.apply(le.fit_transform)
X_test = testData.iloc[:, 0:32]
X_test = X_test.apply(le.fit_transform)

y_train = data.iloc[:, 32:33]
y_test = testData.iloc[:, 32:33]

#Feature Scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

#Training and Predictions
from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(7, 7, 7),max_iter=2000)
mlp.fit(X_train, y_train.values.ravel())

# Make prediction
predictions = mlp.predict(X_test)

# Evaluate
from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))