min = int(input("Digite a quantidade de minutos: "))
if min < 200:
    preco = 0.2
else:
    if min <= 400:
        preco = 0.18
    else:
        if min <= 800:
            preco = 0.15
        else:
            preco = 0.08
conta = min*preco
print("Valor da conta: R$", conta)
