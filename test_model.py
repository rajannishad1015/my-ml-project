import joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

model = joblib.load("model.pkl")

iris = load_iris()
X = iris.data
y = iris.target
_, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

predictions = model.predict(X_test)
acc = accuracy_score(y_test, predictions)

assert acc > 0.9, "Accuracy below 0.9"
print("Test passed. Accuracy:", acc)