linha = coluna = 1
while linha <= 12:
    while coluna <= 12:
        print(linha * coluna, end = "\t")
        coluna = coluna + 1
    print ()
    linha = linha + 1
    coluna = 1
    