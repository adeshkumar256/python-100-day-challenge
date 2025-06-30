# Day 2 challenge
print("Welcome to the tip calculator!")
bill_amount = int(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15?? "))
no_of_people = int(input("How many people to split the bill? "))

each_person_pay = (bill_amount + tip)/no_of_people
print(f"Each person should pay: ${each_person_pay}")
