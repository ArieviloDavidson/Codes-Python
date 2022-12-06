m_qua = int(input("Quantidade de metros quadrados: "))
litros = m_qua / 3
print("Litros necessários para pintar: ", litros)
latas = litros//18
if(litros%18 != 0):
    latas = latas + 1
print("Quantidade de latas necessárias para pintar: ", latas)
valor = latas * 80
print("Valor a ser pago: R$", valor)