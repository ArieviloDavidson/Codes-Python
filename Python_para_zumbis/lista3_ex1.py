nota = float(input("Digite a nota do aluno: "))
while nota < 0 or nota > 10:
    print("Nota inválida!")
    nota = float(input("Digite a nota do aluno: "))