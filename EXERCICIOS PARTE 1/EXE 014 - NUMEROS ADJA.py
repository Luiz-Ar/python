n1 = int(input("Digite um número inteiro: "))
numAdj = False
ultimo = n1 
while n1 > 0 and not numAdj:
    car = n1 % 10
    if car == ultimo:
        numAdj = True
    ultimo = car
    n1 = n1 // 10

if numAdj:
    print("Este número existe numero adjacentes iguais.")
else:
    print("Este número não existe numero adjacentes iguais.")