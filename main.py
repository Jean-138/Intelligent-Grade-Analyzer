# import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# notas = np.array([7,8,5,10])#transforma lista em estrutura Numpy

df = pd.read_csv("students.csv")


# dados =  { "Student": ["Alice", "Bob", "Carol", "David"],
#             "Grade": [7, 8, 5, 10]
# }

# df = pd.DataFrame(dados)

status_list = []



for nota in df["Grade"]:
    if nota >= 7:
        status_list.append("Approved")
    else:
        status_list.append("Reproved")

df["Status"] = status_list



X = df[["Grade"]]
y = df["Status"]

model = KNeighborsClassifier()

model.fit(X, y)

prediction = model.predict([[9]])

print(prediction)


print(df)


# media = df["Grade"].mean()


# media = np.mean(notas)
# maior = np.max(notas)
# menor = np.min(notas)

media = df["Grade"].mean()
maior = df["Grade"].max()
menor = df["Grade"].min()

# if media >= 7:
#     status = "aprovado"
# else:
#     status = "reprovado"

# print("Notas:", notas)
# print("Média:", media)
# print("Maior nota:", maior)
# print("Menor nota:", menor)
# print("Status:", status)





print(media)

