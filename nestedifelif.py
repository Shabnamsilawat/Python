print("Welcome to the rollercoaster:")
height = int(input("Enter your height in cm: "))
age = int(input("Enter your age: "))
if height>=120:
    print("You can ride the rollercoaster")
    if age<=12:
      print("You have to pay $5.")
    elif age<=18:
     print("You have to pay $7.")
    else:
     print("You have to pay $12.")
else:
  print("You cannot ride the rollercoaster")