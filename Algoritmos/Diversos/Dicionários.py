# Criação de um dicionário de filmes, onde as chaves são os títulos dos filmes e os valores são os anos de lançamento.
filmes = {
    "Star Wars: Episódio IV - Uma Nova Esperança": 1977,
    "Indiana Jones e Os Caçadores da Arca Perdida": 1981,
    "Jurassic Park": 1993,
    "Harry Potter e a Pedra Filosofal": 2001,
    "Vingadores: Ultimato": 2019
}

# Imprime o dicionário de filmes completo
print(filmes)

# Acessa um valor específico do dicionário utilizando uma chave
print("O filme 'Jurassic Park' foi lançado em", filmes["Jurassic Park"])

# Adiciona um novo item ao dicionário
filmes["O Senhor dos Anéis: A Sociedade do Anel"] = 2001

# Modifica o valor de um item existente no dicionário
filmes["Star Wars: Episódio IV - Uma Nova Esperança"] = 1978

# Imprime o dicionário atualizado
print(filmes)

# Percorre todos os itens do dicionário utilizando um laço de repetição for
for filme, ano in filmes.items():
    print(filme, "foi lançado em", ano)
