print("Welcome to Body Mass index Calculator!😊")
print("You are required to choose the unit")

height_unit= str(input("For height:\nIt is either meter or feet: ")).lower()
weight_unit=str(input("For weight:\nIt is either pounds or kilogram: ")).lower()
print("Please enter your details below")

if height_unit == "meter":
    height = float(input("Enter your height in meters: "))
    Rounded_height=round(height, 2)

elif height_unit == "feet":
    height = float(input("Enter your height in feet: ")) * 0.3048
    Rounded_height=round(height, 2)
else:
    print("Invalid input")
    exit()

if weight_unit== "pounds":
    weight = float(input("Enter your weight in pounds: "))
    Rounded_weight=round(weight, 2)
elif weight_unit == "kilograms":
    weight = float(input("Enter your weight in kilograms: "))*0.453592
    Rounded_weight=round(weight, 2)
else:
    print("Invalid input")
    exit()

print(f"If weight is: {Rounded_weight} and height is: {Rounded_height}")
#BMI= int(weight)/ float(height)
#print (f"The BMI is: {BMI}")
#print(round(BMI))
BMI= weight/(height **2)
BMI=round(BMI)

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
if BMI >18.5 and  BMI< 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
if BMI > 25 and BMI<30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
if BMI > 30 and BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
if BMI > 35:
    print(f"Your BMI is {BMI}, you are clincally obese.")