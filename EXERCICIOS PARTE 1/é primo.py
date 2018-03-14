k = int(input("Digite um número inteiro: "))
div = 1
i = 2
divisores = 0
maxprimo = 1
while div <= k or i < k:
    if i % div == 0:
        divisores = divisores + 1
        div = div + 1
        if divisores > 2:
            i = i + 1
            div = 1
        if divisores == 2 and i == div:
            maxprimo = i
    else:
        div = div + 1
print(maxprimo)
        