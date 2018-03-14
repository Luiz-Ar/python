def cria_matriz(n_linhas, n_colunas):
    '''(int, int, valor) -> matriz(lista de listas) 
    Cria e retorna uma matriz com n_linhas linhas e n_colunas colunas em que cada elemento é digitado pelo usuário.'''
    matriz = [] #lista vazia
    for i in range(n_linhas):
        #cria a linha i
        linha = [] #lista vazia
        for h in range(n_colunas):
            valor = int(input("Digite o elemento da linha e coluna: [" + str(i) + "][" + str(h) + "]: "))
            linha.append(valor)
        
        #adiciona linha à matriz
        matriz.append(linha)
    print(matriz)
    return matriz

def main():
    linha = int(input("Digite o número de linhas: "))
    col = int(input("Digite o número de colunas: "))
    return cria_matriz(linha, col)

main()