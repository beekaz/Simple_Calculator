print("\tWelcome to tip calculator")
print("Guess you need my assistance spilting your bill equally😊")
total_bill= float(input("\nWhat is the total bill? "))
#tip_percent=()
if 0 >= total_bill <=129:
    standard_tip=15
    print(f"I suggest you use the standard {15}% tip")
    decision=str(input("should i go on?\nyes/no "))
    if decision=="yes":
        tip_percent= standard_tip
    else:
        custom_tip_percent=float(input("Enter custom tip %: "))
        tip_percent=custom_tip_percent
        print(f" I will be using (tip_percent)%")
elif 130 >= total_bill <290:
    standard_tip=20
    print(f"I suggest you use the standard {20}% tip.")
    decision=str(input("Should I go on?\n(yes/no) "))
    if decision=="yes":
        tip_percent= standard_tip
    else:
        custom_choice=float(input("Enter custom tip %: "))
        tip_percent=custom_choice
    print(f"I will be using (tip_percent)%")
else:
    custom_choice=float(input("Enter custom tip %: "))
    tip_percent=custom_choice
    print(f"I will be using (tip_percent)%")
number_of_individuals=int(input("How many people to spilt the bill ? "))
total_tip= total_bill + tip_percent/100
individuals_bill= total_tip/number_of_individuals
rounded_value= round(individuals_bill, 1)
print(f"Each person would pay {rounded_value} naira")
#print("{:.1f}".format(individuals_bill))