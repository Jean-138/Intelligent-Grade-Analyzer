import numpy as np

notas = np.array([7,8,5,10])#transforma lista em estrutura Numpy

media = np.mean(notas)
maior = np.max(notas)
menor = np.min(notas)

if media >= 7:
    status = "aprovado"
else:
    status = "reprovado"

print("Notas:", notas)
print("Média:", media)
print("Maior nota:", maior)
print("Menor nota:", menor)
print("Status:", status)