print("Welcome to the rollercoaster!")
height = int(input("Enter your height in cm: "))
age = int(input("Enter your age: "))
bill = 0
if height>=120:
    print("You can ride the rollercoaster: ")
    if age<=12:
        bill = 5
        print("You have to pay $5")
    elif age<=18:
        bill = 7
        print("You have to pay $7")
    else:
        bill = 12
        print("You have to pay $12")
        want_photo= input("Do you want a photo if Yes type y if No type n:")
    if want_photo == "y":
        bill+=3
        print(f"Your total bill is: {bill}")
else:
    print("You cannot ride the rollercoaster: ")