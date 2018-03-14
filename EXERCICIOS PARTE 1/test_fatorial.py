def fatorial (n):   
    i = fat = 1
    while i <= n:
        fat = fat * i
        i = i + 1
    return fat

def fatorial0():
    assert fatorial(0)  == 1
def fatorial1():
    assert fatorial(1)  == 1
def fatorial_negativo():
    assert fatorial(-10)  == 0
def fatorial4():
    assert fatorial(0)  == 24
def fatorial5():
    assert fatorial(0)  == 120