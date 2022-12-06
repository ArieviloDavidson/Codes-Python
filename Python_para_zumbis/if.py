velocidade = int(input("Digite a velocidade do carro: "))
if velocidade > 110:
    print("O carro foi multado!!!")
    valor = (velocidade - 110)*5
    print("Valor da multa: R$", valor)