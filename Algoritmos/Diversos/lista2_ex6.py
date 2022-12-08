hora_trab = int(input("Salário por hora: "))
horas = int(input("Horas trabalhadas no mês: "))
s_bruto = hora_trab * horas
print("Salário bruto: R$", s_bruto)
im_renda = s_bruto*0.11
inss = s_bruto*0.08
sind = s_bruto*0.05
print("Valor do imposto de renda: ", im_renda)
print("Valor do INSS: ", inss)
print("Valor sindicato: ", sind)
s_liq = s_bruto - im_renda - inss - sind
print("Salário Líquido: ", s_liq)