n = int(input("Entre um néumro inteiro:"))
if n % 5 == 0 and n % 3 == 0:
    print("FizzBuzz")
else:
    if n % 5 == 0:
        print("Buzz")
    else:
        if n % 3 == 0:
            print("Fizz")
        else:
            print(n)