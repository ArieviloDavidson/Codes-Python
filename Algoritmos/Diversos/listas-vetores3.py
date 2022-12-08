notas = []
k = 1
while k <= 4:
    notas.append(float(input("Nota: ")))
    k = k + 1
soma = k = 0
while k <= 3:
    soma = soma + notas[k]
    k = k + 1
print("Média: ", soma/4)