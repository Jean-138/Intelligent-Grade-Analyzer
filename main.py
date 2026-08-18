import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

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

X_train, X_test, y_train, y_test = train_test_split(X, y)

model = KNeighborsClassifier(n_neighbors=3)

model.fit(X_train, y_train)

prediction = model.predict(X_test)

accuracy = accuracy_score(y_test, prediction)

print("Accuracy:", accuracy)
print("Prediction:", prediction)
print("Actual:", y_test.values)