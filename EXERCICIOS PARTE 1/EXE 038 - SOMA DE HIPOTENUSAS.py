import math
def soma_hipotenusas(n):
    a = 1
    b = 1
    hipotenusa = 1
    valor = 0
    while hipotenusa <= n:
        b = 1
        while a <= n and b <= n:
            hip = math.sqrt(a ** 2 + b ** 2)
            if hipotenusa == hip and hipotenusa <= n:
                valor = hipotenusa + valor
                hipotenusa = hipotenusa + 1
            else:
                a = a + 1
            if a == n:
                b = b + 1
                a = 1
        a = 1
        b = 1
        hipotenusa = hipotenusa + 1
    return(valor)
            
        
        
    
