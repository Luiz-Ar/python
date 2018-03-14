n = 1
while n >= 0:
    n = int(input("Entre um número inteiro: "))
    fator = 1
    while n > 1:
        fator = fator * n
        n = n - 1
    print(fator)      