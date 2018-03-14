n1 = int(input("Digite um número inteiro: "))
soma = 0
while n1 > 0:
    car = n1 % 10
    n1 = n1 // 10
    soma = soma + car
print("A soma dos número é: ", soma)