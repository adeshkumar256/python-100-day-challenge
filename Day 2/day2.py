# Day 2 challenge
def get_bill_amount():
    while True:
        try:
            value = float(input("What was the total bill? $"))
            if value > 0:
                return value
            else:
                print("Bill amount must be greater than 0. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_tip():
    while True:
        try:
            tip = int(
                input("How much tip would you like to give? $"))
            if tip < bill:
                return tip
            else:
                print("Please give less tip")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_number_of_people():
    while True:
        try:
            value = int(input("How many people to split the bill? "))
            if value > 0:
                return value
            else:
                print("Number of people must be greater than 0. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def calculate_each_person_pay(bill_amount, tip, no_of_people):
    total_bill = bill_amount + tip
    return round(total_bill / no_of_people, 2)


print("Welcome to the tip calculator! \n\n")
bill = get_bill_amount()
tip = get_tip()
people = get_number_of_people()
each_pay = calculate_each_person_pay(bill, tip, people)
print(f"Each person should pay: ${each_pay}")
