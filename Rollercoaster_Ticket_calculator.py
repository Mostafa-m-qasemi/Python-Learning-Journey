print("Welcome to the rollercoster!")
height = int(input("How tall are you? "))
age = int(input("How old are you? "))
bill = 0

if height >= 120:
    print("you can ride")
    if age < 12:
        print("child ticket is $5.")
        bill += 5
    elif age < 18:
        print("youth ticket is $7.")
        bill += 7
    elif 45 <= age <= 55:
        print("have a free ride")
        bill += 0
    else:
        print("adult ticket is $12.")
        bill += 12
    photo = input("Do you wanna photo? y or n ")
    if photo == "y":
        bill += 3
    print(f"your ticket is ${bill}")
else:
    print("sorry, you are not tall enough")
