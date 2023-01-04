soma = 0
cont = 0
while True: # Loop infinito para testar o comando break;
    x = int(input("n (zero sai): "))
    if x == 0:
        break
    soma = soma + x
    cont = cont + 1
print ("Soma: ", soma)
media = soma/cont
print("Média: ", media)