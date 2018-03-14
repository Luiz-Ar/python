n = 1
fator = 1

def fatorial(n):
    while n > 1:
        fator = fator * n
        n = n - 1
    return(fator)  

while n >= 0:
    n = int(input("Entre um número inteiro: "))
    fator = 1
    fatorial(n)     