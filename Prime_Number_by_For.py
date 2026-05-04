num = int(input("Enter your number: "))
counter = 0
for i in range(1,num+1):
    if num % i == 0:
        counter += 1

if counter == 2:
    print("This is a Prime Number")
else:
    print("This is not a Prime Number")
