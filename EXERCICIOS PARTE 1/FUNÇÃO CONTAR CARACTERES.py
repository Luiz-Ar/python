def total_caracteres(a, b):
    espaços = a.count(b)
    total = len(a)
    total_de_letras = total - espaços
    return(total_de_letras)

def total_words(a):
    words = a.split()
    return len(words)

def media_word():
    c = total_caracteres(a, b)
    d = total_words(a)
    media = c / d
    print(media)

a = input("Entre um texto: ")
b = " "


media_word()
