def sao_multiplicaveis(m1, m2):
    if len(m1[0]) == len(m2):
        print("Coluna do primeiro é igual a linha do segundo")
        return True
    elif len(m1) == len(m2[0]):
        print("Coluna do segundo é igual a linha do primeiro")
        return True
    else:
        return False