# split transforma uma variável em vetor
mes = "janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro".split() # Podemos não passar parâmetro nenhum que o código entenderá o espaçamento
# split também separa um input em mais de uma variável
d,m,a = input("dd/mm/aaaa: ").split("/") # ou podemos passar um caractere ou mais que vai ser usado como split e ignorado no input
print(d, "de", mes[int(m)-1], "de", a)