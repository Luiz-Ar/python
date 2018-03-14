n = int(input("Digite um número inteiro: "))

if n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0:
    print("primo")
else:
    print("não primo")