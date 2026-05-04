num = int(input("Enter your number: "))
is_prime = True
if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
if is_prime:
    print("This is a Prime Number")
else:
    print("This is not a Prime Number")
