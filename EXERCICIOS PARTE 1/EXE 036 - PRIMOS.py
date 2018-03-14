fator = 1
multiplicidade = 0
n = int(input("Entre um número inteiro"))
while n > 1:
    if n % fator == 0:
        multiplicidade = multiplicidade + 1
        if fator == n:
            if multiplicidade == 2:
                print(n)
            n = n - 1
            multiplicidade = 0
            fator = 0
    fator = fator + 1