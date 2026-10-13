import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df = pd.read_csv("students.csv")

status_list = []

for nota in df["Grade"]:
    if nota >= 7:
        status_list.append("Approved")
    else:
        status_list.append("Reproved")

df["Status"] = status_list

X = df[["Grade"]]
y = df["Status"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=42, stratify=y)

model = KNeighborsClassifier(n_neighbors=3)

model.fit(X_train, y_train)

prediction = model.predict(X_test)

accuracy = accuracy_score(y_test, prediction)

matrix = confusion_matrix(y_test, prediction)

report = classification_report(y_test, prediction)

print("Accuracy:", accuracy)
print("Prediction:", prediction)
print("Actual:", y_test.values)


print(matrix)

print("Confusion Matrix:")
print(matrix)

print("Classification Report:")
print(report)