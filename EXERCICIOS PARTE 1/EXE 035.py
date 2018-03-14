linha = coluna = 1
largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

while linha <= altura:
    while coluna <= largura:
        if linha == 1 or linha == altura or coluna == 1 or coluna == largura:
            print("#", end = "")
        else:
            print(" ", end = "")
        coluna = coluna + 1
    print ()
    linha = linha + 1
    coluna = 1