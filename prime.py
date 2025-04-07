num = int(input("Enter a number to check for prime: "))
if num <= 1:
    print("Not a Prime Number")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")