linha = coluna = 1
largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

while linha <= altura:
    while coluna <= largura:
        print("#", end = "")
        coluna = coluna + 1
    print ()
    linha = linha + 1
    coluna = 1