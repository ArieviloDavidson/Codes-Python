a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
if a > b and a > c:
    print("Maior valor: ", a)
    if b < c:
        print("Menor valor: ", b)
    else:
        print("Menor valor: ", c)
if b > a and b > c:
    print("Maior valor: ", b)
    if a < c:
        print("Menor valor: ", a)
    else:
        print("Menor valor: ", c)
if c > a and c > b:
    print("Maior valor: ", c)
    if a < b:
        print("Menor valor: ", a)
    else:
        print("Menor valor: ", b)
if a == b > c:
    print("Maior valor: ", a)
    print("Menor valor: ", c)
if a == c > b:
    print("Maior valor: ", a)
    print("Menor valor: ", b)
if b == c > a:
    print("Maior valor: ", b)
    print("Menor valor: ", a)
if a == b == c:
    print("Os três valores são iguais")