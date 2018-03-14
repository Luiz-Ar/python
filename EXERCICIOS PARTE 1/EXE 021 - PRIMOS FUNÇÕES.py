n = 1
def primos(n):
    n = int(input("Número inteiro: ")) 
    divisor = 2
    multiplicidade = 0
    while divisor <= n:
        if n % divisor == 0:
            multiplicidade = multiplicidade + 1
            divisor = divisor + 1
        divisor = divisor + 1
    if multiplicidade > 2:
        print("O número não é primo.")
    else:
        print("O número é primo")

primos(n)