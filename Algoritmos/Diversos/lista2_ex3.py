peso = float(input("Digite o peso: "))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
else:
    excesso = 0
    multa = 0
print("Peso em excesso: ", excesso)
print("Multa: R$", multa)