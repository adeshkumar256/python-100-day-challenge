# Day 2 challenge
def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Value must be greater than 0. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_tip_percentage():
    while True:
        try:
            tip = int(
                input("How much tip would you like to give? 10, 12, or 15? "))
            if tip in [10, 12, 15]:
                return tip
            else:
                print("Please enter 10, 12, or 15.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Value must be greater than 0. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def calculate_each_person_pay(bill_amount, tip_percent, no_of_people):
    total_bill = bill_amount + (bill_amount * tip_percent / 100)
    return round(total_bill / no_of_people, 2)


print("Welcome to the tip calculator!")
bill = get_positive_float("What was the total bill? $")
tip = get_tip_percentage()
people = get_positive_int("How many people to split the bill? ")
each_pay = calculate_each_person_pay(bill, tip, people)
print(f"Each person should pay: ${each_pay}")
