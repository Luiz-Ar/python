def primos(n):
    n = int(input("Número inteiro: ")) 
    fator = 2
    multiplicidade = 0
    while fator <= n:
        if n % fator == 0:
            multiplicidade = multiplicidade + 1
            fator = fator + 1
        fator = fator + 1
    if multiplicidade > 2:
        print("O número não é primo.")
    else:
        print("O número é primo")
n = 1        
primos(n)