








populacao = populacao_inicial()

while True:
    for i in range(N - N_elite):
        pai1 = seleciona(populacao)
        pai2 = seleciona(populacao)
        filho = cruzamento(pai1, pai2)
        if (prob() < taxa_de_mutacao):
            filho = mutacao(filho)
        prox_geracao.append(filho)
    populacao = prox_geracao + elite