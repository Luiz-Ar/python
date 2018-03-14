def inicio():
    print("SEJA BEM VINDO AO JOGO DE NIM. ESCOLHA:")
    escolha = int(input("1 - Para jogar uma partida amistosa\n 2 - Para jogar um campeonato "))
    if escolha == 1
        partida(n, m) 

def partida():

    print("PARTIDA")

    n = int(input("Quantas peças? "))
    m = int(input("Quantas jogadas? "))

    
    vez_do_computador = True

    if n % (m+1) == 0: vez_do_computador = False

    while n > 0:

        if vez_do_computador:
            jogada = computador_escolhe_jogada(n, m)
            vez_do_computador = False
            print("Computador retirou {} peças.".format(jogada))
        else:
            jogada = usuario_escolhe_jogada(n, m)
            vez_do_computador = True
            print("Você retirou {} peças.".format(jogada))

        n = n - jogada

        print("Restam apenas {} peças em jogo.\n".format(n))

    if vez_do_computador:
        print("Você ganhou!")
        return 1
    else:
        print("O computador ganhou!")
        return 0


def usuario_escolhe_jogada(n, m):
    print("Sua vez!\n")
    jogada = 0
    while jogada == 0:
        jogada = int(input("Quantas peças irá tirar? "))
        if jogada > n or jogada < 1 or jogada > m:
            jogada = 0
    return jogada

def computador_escolhe_jogada(n, m):
    print("Vez do computador!")
    if n <= m:
        return n
    else:
        quantia = n % (m+1)
        if quantia > 0:
            return quantia
        return m