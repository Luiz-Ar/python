def soma_elementos(lista):
    soma = 0
    tamanho = len(lista) - 1
    while tamanho >= 0:
        soma = (lista[tamanho]) + soma
        tamanho = tamanho - 1
    return(soma)