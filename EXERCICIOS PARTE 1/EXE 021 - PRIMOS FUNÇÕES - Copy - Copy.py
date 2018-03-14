def fizzbuzz(n):
    if n % 3:
        return("Fizz")
    elif n % 5:
        return("Buzz")
    elif n % 3 and n % 5:
        return("FizzBuzz")
    else:
        return(n)
        
    
