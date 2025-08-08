print("Welcome to Python Pizza Deliveries!")

size = input("Enter the size of the pizza you want, S , M or L\n")
pepperoni = input("Do you want extra pepperoni? Y for yes and N for no.\n")
cheese = input("Do you want extra cheese? Y for yes and N for no.\n")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Invalid input has been entered.")
    bill = 0

# These should be outside the else block
if pepperoni == "Y":
    if size == "S":
        bill += 2
    elif size == "M" or size == "L":
        bill += 3

if cheese == "Y":
    bill += 1

print(f"Your total bill is: ${bill}")
