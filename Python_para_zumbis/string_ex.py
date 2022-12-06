from hashlib import algorithms_guaranteed


palavra = input("Digite uma palavra: ")
if(palavra == palavra[::-1]):
    print("PALÍNDROMO!!!")
else:
    print("Não é um palíndromo!")