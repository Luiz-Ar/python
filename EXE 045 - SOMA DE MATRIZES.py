def dimensoes(matriz):
    b = len(matriz)    
    if b == 1:
        c = len(matriz[0])
    elif len(matriz[1]) == len(matriz[0]):
        c = len(matriz[0])
      
    return(b, c)

def soma_matrizes(m1, m2):
    somav = False
    if dimensoes(m1) == dimensoes(m2):
        somav = True
        soma_matrizes = []
        quant_linhas = len(m1)
        quant_colunas = len(m1[0])
        for i in range(quant_linhas):
            soma_matrizes.append([])
            for j in range(quant_colunas):
                soma = m1[i][j] + m2[i][j]
                soma_matrizes[i].append(soma)
        return(soma_matrizes)
    else:
        return(somav)
