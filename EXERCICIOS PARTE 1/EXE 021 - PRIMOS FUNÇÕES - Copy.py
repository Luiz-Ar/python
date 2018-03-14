i = max = 2
n = int(input("Digite um número inteiro: "))
    
while i <= n:
    if i < 4 and i % 3 == 0:
        max = i
        i = i + 1
    if i < 6 and i % 5 == 0:
        max = i
        i = i + 1
    if i < 8 and i % 7 == 0:
        max = i
        i = i + 1
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
        max = i
        i = i + 1
    else:
        i = i + 1
print(max)

