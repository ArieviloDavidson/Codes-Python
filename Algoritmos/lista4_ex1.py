import random

var = random.sample(range(100), 10)

max = var[0]
min = var[0]

for k in range(10):
    print(var[k])
    if(var[k] > max):
        max = var[k]
    if(var[k] < min):
        min = var[k]

print("Valor Máximo: ", max)
print("Valor Mínimo: ", min)