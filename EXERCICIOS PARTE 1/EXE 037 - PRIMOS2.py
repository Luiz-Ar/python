def n_primos(n):
    fator = 1
    multiplicidade = 0
    primos = 0
    while n > 1:
        if n % fator == 0:
            multiplicidade = multiplicidade + 1
            if fator == n:
                if multiplicidade == 2:
                    primos = primos + 1
                n = n - 1
                multiplicidade = 0
                fator = 0
        fator = fator + 1
    return(primos)
