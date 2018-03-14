lista = []
n = int(input("Entre uma lista de números terminada em 0: "))
while n > 0:
    lista.append(n)
    n = int(input("Entre outro número: "))
tamanho = len(lista) - 1
while tamanho >= 0:
    print(lista[tamanho])
    tamanho = tamanho - 1
