def cria_matriz(n_linhas, n_colunas, valor)
    '''(int, int, valor) -> matriz(lista de listas) 
    Cria e retorna uma matriz com n_linhas linhas e n_colunas colunas em que cada elemento é igual ao valor dado.'''
    matriz = [] #lista vazia
    for i in range(n_linhas):
        #cria a linha i
        linha = [] #lista vazia
        for h in range(n_colunas):
        linha.append(valor)
        
        #adiciona linha à matriz
        matriz.append(linha)
    return matriz