a = int(input("Digite o primeiro lado: "))
b = int(input("Digite o segundo lado: "))
c = int(input("Digite o terceiro lado: "))
if a + c > b and a + b > c and b + c > a:
    print("Os lados formam um triângulo!")
    if a != b != c:
        print("Tipo de triângulo = Escaleno")
    elif a == b == c:
        print("Tipo de triângulo = Equilátero")
    else:
        print("Tipo de triângulo = Isósceles")
else:
    print("Os lados não formam um triângulo!")