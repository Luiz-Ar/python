def sao_multiplicaveis(m1, m2):
    multiplicav = False
    if len(m1) == len(m2[0]) and len(m1) != len(m2) and len(m2) == len(m1[0]):
        multiplicav = True
    elif len(m1) == len(m2) and len(m2[0]) != len(m1[0]):
        multiplicav = True
    elif len(m1) == 1 and len(m2) == 1:
        multiplicav = True
    return(multiplicav)

