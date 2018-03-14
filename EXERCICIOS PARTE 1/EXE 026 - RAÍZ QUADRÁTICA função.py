import math

def delta(a, b, c):
    return b ** 2 - 4 * a * c

def main():
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

main()