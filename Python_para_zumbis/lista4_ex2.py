import random

def épar(x):
    return x%2 == 0

var = random.sample(range(100), 20)

print("Lista de Sortidos: ", var)

par = []
impar = []

for k in range(20):
    if(épar(var[k])):
        par.append(var[k])
    else:
        impar.append(var[k])

print("Pares: ", par)
print("Ímpares: ", impar)
    