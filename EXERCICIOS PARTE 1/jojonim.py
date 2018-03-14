def inicio():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("")
    print("1 - para jogar uma partida isolada")
    Partida = int(input("2 - para jogar um campeonato "))

    if Partida == 2:
        print("")
        print("Voce escolheu um campeonato!")
        print("")
        campeonato()
    elif Partida == 1:
        print()
        partida()
    else:
        print("")
        print("Escolha Inválida. Tente novamente!")
        print("")
        inicio()

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    PCturn = False
    if n % (m+1) == 0:
        print()
        print("Voce começa!")
    else:
        print()
        print("Computador começa!")
        PCturn = True
    while n > 0:
        if PCturn:
            PCmove = computador_escolhe_jogada(n, m)
            n = n - PCmove
            if PCmove == 1:
                print()
                print("O computador tirou uma única peça")
            else:
                print()
                print("O computador tirou", PCmove, "peças")
            PCturn = False
        else:
            USERmove = usuario_escolhe_jogada(n, m)
            n = n - USERmove
            if USERmove == 1:
                print()
                print("Você tirou uma única peça")
            else:
                print()
                print("Você tirou", USERmove, "peças")
            PCturn = True
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
            print()
        else:
            if n != 0:
                print("Agora restam,", n, "peças no tabuleiro.")
                print()

    print("Fim do jogo! O computador ganhou!")
    

def campeonato():
    nRodada = 1
    while nRodada <= 3:
        print()
        print("** Rodada", nRodada, "**")
        print()
        partida()
        nRodada = nRodada + 1
    print()
    print("Placar: Você 0 X 3 Computador")
    
def computador_escolhe_jogada(n, m):
    PCmove = 1
    while PCmove != m:
        if (n - PCmove) % (m+1) == 0:
            return PCmove
        else:
            PCmove += 1
    return PCmove

def usuario_escolhe_jogada(n, m):
    UserJogada = False

    while not UserJogada:
        USERmove = int(input("Quantas peças você vai tirar? "))
        if USERmove > m or USERmove < 1:
            print()
            print("Jogada inválida! Tente novamente.")
            print()

        else:
            UserJogada = True

    return USERmove

inicio()