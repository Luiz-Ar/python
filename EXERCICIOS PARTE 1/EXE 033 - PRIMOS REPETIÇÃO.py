fator = 1
multiplicidade = 0
n = int(input("Entre um número inteiro positivo: "))
while n > 0:
    while fator <= n:
        if n % fator == 0:
            multiplicidade = multiplicidade + 1
            fator = fator + 1
        fator = fator + 1
    if multiplicidade > 2:
        print("O número não é primo.")
    else:
        print("O número é primo")
    n = int(input("Entre um número inteiro positivo: "))
    multiplicidade = 0
    fator = 2