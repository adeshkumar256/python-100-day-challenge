# Day 1 challenge
# Ask users to enter the name of the city they were born in
# ask users for their pet's name
# return the name of the group suggestion as city + pet name
# check for blank responses

from colorama import Fore, Back, Style


def get_user_city():
    city = ""
    while city == "":
        city = input("What's the name of the city you grew up?")
        if city == "":
            print(
                "City cannot be blank or just spaces. Please enter a valid name.".upper())
        else:
            break
    return city


def get_pet_name():
    pet_name = ""
    while True:
        pet_name = input("What's your pet's name?").strip()
        if pet_name == "":
            print(
                "Pet name cannot be blank or just spaces. Please enter a valid name.".upper())
        else:
            break
    return pet_name


def display_suggestion():
    city = get_user_city()
    pet_name = get_pet_name()
    group_name = f"{city}_{pet_name}"
    print(
        f"You can name your group as {Fore.GREEN}{group_name}{Style.RESET_ALL}")


display_suggestion()
