def imprime_matriz(matriz):
    quant_linhas = len(matriz)
    quant_colunas = len(matriz[0])
    for i in range(quant_linhas):
        for j in range(quant_colunas):
            if j != (quant_colunas - 1):
                print(matriz[i][j], end=' ')
            else:
                print(matriz[i][j])
    
