import re

def total_caracteres(a, b):
    espaços = a.count(b)
    total = len(a)
    total_de_letras = total - espaços
    return(total_de_letras)

def total_words(a):
    words = a.split()
    return len(words)

def separa_palavras(frase):
    frase = a.split()
    return(len(frase))


def total_words2(a):
    lista_palavras = a.split()
    return (lista_palavras)
    n_palavras_diferentes(lista_palavras)

def media_word():
    c = total_caracteres(a, b)
    d = total_words(a)
    media = c / d
    print("Tamanho médio das palavras: ", media)


def n_palavras_diferentes(lista_palavras):
    freq = dict()
    for palavra in total_words2(a):
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
    return(len(freq))

def n_palavras_unicas(lista_palavras):
    freq = dict()
    unicas = 0
    for palavra in total_words2(a):
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1
    return(unicas)

def type_token():
    h = separa_palavras(total_words2(a))
    i = n_palavras_diferentes(total_words(a))
    type_token = i / h
    print("Relação Type-Token: ", type_token)

def hapax_legomana():
    f = separa_palavras(total_words2(a))
    g = n_palavras_unicas(total_words2(a))
    hapax = g / f
    print("Razão Hapax Legomana: ", hapax)

def separa_sentencas(a):
    sentencas = re.split(r'[.!?]+', a)
    if sentencas[-1] == '':
        del sentencas[-1]
    return(len(sentencas))

def media_sentencas():
    j = separa_palavras(total_words2(a))
    k = separa_sentencas(a)
    media_sentenca = j / k
    print("Média de Sentenças: ", media_sentenca)

a = input("Entre um texto: ")
b = " "

media_word()
n_palavras_unicas(total_words2(a))
type_token()
hapax_legomana()
media_sentencas()
