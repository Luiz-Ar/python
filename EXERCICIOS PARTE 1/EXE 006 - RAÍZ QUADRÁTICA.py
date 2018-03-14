import math
a = float(input("Entre o valor de a: "))
b = float(input("Entre o valor de b: "))
c = float(input("Entre o valor de c: "))
delta = b ** 2 - 4 * a * c
if delta >= 0:
    x1 = (- b + math.sqrt(delta)) / (2 * a)
    x2 = (- b - math.sqrt(delta)) / (2 * a)
else:
    print("Essa função não tem raízes reais!")
if delta == 0:
    print("A raíz da equação é ", x1)
else:
    if delta > 0:
        print("As raízes da equação são ", x1, "e", x2)   