trem = []
trem.append(42)
trem.append("Abacate")
trem.append(3.14)
print(trem)
print(len(trem))
notas = [6, 7, 8, 9, 10]
soma = 0
cont = 0
while cont < len(notas):
    soma = soma + notas[cont]
    cont = cont + 1
media = soma/len(notas)
print("Média = ", media)