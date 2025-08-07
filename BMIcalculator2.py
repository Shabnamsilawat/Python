print("Welcome to BMI calculator!")
height = float(input("Enter your height:"))
weight = int(input("Enter your weight: "))
bmi = weight/height**2
print(f"Your BMI is :{bmi} ")
if bmi>=18.5:
    print("Normal weight.")
elif bmi>=25:
    print("overweight")
else:
    print("Under weight:")