n1 = int(input("Entre um número: "))
n2 = int(input("Entre outro número: "))
n3 = int(input("Entre outro número: "))

if n1 < n2 and n2 < n3:
    print("crescente")
else:
    print("não está em ordem crescente")