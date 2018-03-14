import math
n = 1

def repeat():
    print("\n\n")
    print("Você gostaria de fazer mais alguma coisa?")
    print("Sim[S] ou Não[N]?\n\n")
    repeat = input()
    if repeat == "S" or repeat == "s":
        print("\n\n")
        main()

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
    
    repeat()
        
def fatores_primos(n):
    n = int(input("Número inteiro: ")) 
    fator = 2
    multiplicidade = 0
    while n > 1:
        while n % fator == 0:
            n = n / fator
            multiplicidade = multiplicidade + 1
        if multiplicidade > 0:
            print("Fator", fator, "Multiplicidade =", multiplicidade)
        fator = fator + 1
        multiplicidade = 0
    repeat()
    
def delta(a, b, c):
    return b ** 2 - 4 * a * c

def bhaskara():
    a = float(input("Entre o valor de a: "))
    b = float(input("Entre o valor de b: "))
    c = float(input("Entre o valor de c: "))
    raízes(a, b, c)

def raízes(a, b, c):
    d = delta(a, b, c)
    if d >= 0:
        x1 = (- b + math.sqrt(d)) / (2 * a)
        x2 = (- b - math.sqrt(d)) / (2 * a)
    else:
        print("Essa função não tem raízes reais!")
    if d == 0:
        print("A raíz da equação é ", x1)
    elif d > 0:
        print("As raízes da equação são ", x1, "e", x2)
    repeat()

def main():
    print("O que você deseja fazer?")
    print("")
    print("1 - Equação de 2 grau")
    print("2 - Fatoração em números primos")
    print("3 - Verificar se número é primo")
    escolha = int(input())
    
    if escolha == 1:
        bhaskara()
    elif escolha == 2:
        fatores_primos(n)
    elif escolha == 3:
        primos(n)
    else:
        print("Escolha inválida. Tente novamente.")
        main()
            
    
main()