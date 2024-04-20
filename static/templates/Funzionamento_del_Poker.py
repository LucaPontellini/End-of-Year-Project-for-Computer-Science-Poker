import os
import random
from tabulate import tabulate

def deck_creation (seeds: list, values_of_cards: list) -> list[dict]:

    """This function creates the deck"""

    deck = []

    for seed in seeds:
        for value in values_of_cards:
            deck.append({"seed": seed, "value": value})
    return deck

def deck_shuffle(deck):

    """This feature shuffles the deck"""

    for _ in range(random.randint(10, 15)):
        random.shuffle(deck)
    return deck

def draw_card(deck: list[dict]) -> dict: # type: ignore

    """This function draws a card from the deck"""

    if len(deck) > 0:
        card = deck.pop(0)
        
        print(card)
        return card

def chip_table (value_of_chips) -> list:

    """This feature creates and prints a poker chip table"""

    chips_list = []

    for color, value in value_of_chips.items():
        chips_list.append([color, value])

    print(tabulate(chips_list, headers=['Color', 'Value'], tablefmt='grid'))
    return chips_list

def cashier(value_of_chips) -> dict:

    """This function collects the number of each color of poker chips from the user"""

    total_money = float(input("Enter the total amount of money you want to convert to chips: "))
    remaining_money = total_money

    chips_dict = {}

    for color in value_of_chips.keys():
        while True:

            print(f"You have ${remaining_money} remaining.")

            num_chips = int(input(f"How many {color} chips do you want? "))
            chip_value = int(value_of_chips[color][1:].replace(",", ""))

            if num_chips * chip_value <= remaining_money:
                remaining_money -= num_chips * chip_value
                chips_dict[color] = num_chips
                break
            else: print("You don't have enough money for that many chips. Please enter a smaller number.")

    print(tabulate([[color, number] for color, number in chips_dict.items()], headers=['Color', 'Number'], tablefmt='grid'))
    print(f"You have ${remaining_money} remaining.")
    return chips_dict, remaining_money # type: ignore

def display_user_table(chips_dict, remaining_money, value_of_chips):

    """This function displays the user's chips and remaining money in a table"""

    os.system('cls' if os.name == 'nt' else 'clear')

    user_table = []

    total_money = remaining_money

    for color, number in chips_dict.items():
        chip_value = int(value_of_chips[color][1:].replace(",", ""))
        total_money += number * chip_value
        user_table.append([color, number, f"${number * chip_value}"])

    user_table.append(["Total", "", f"${total_money}"])
    user_table.append(["Remaining Money", "", f"${remaining_money}"])

    print(tabulate(user_table, headers=['Color', 'Number', 'Value'], tablefmt='grid'))

def convert_back(chips_dict, value_of_chips):

    """This function converts chips back to money"""

    total_money = 0

    for color, number in chips_dict.items():
        chip_value = int(value_of_chips[color][1:].replace(",", ""))
        total_money += number * chip_value

    print(f"You have converted your chips back to ${total_money}.")
    return total_money

def main():

    seeds = ['hearts', 'diamonds', 'clubs', 'spades']
    values_of_cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    deck = deck_creation(seeds, values_of_cards)
    deck = deck_shuffle(deck)

    value_of_chips = {
        "White": "$1",
        "Red": "$5",
        "Blue": "$10",
        "Green": "$25",
        "Black": "$100",
        "Purple": "$500",
        "Yellow": "$1000",
        "Pink": "$5000",
        "Light Blue": "$10000"
    }

    while True:
        convert_money = input("Do you want to convert money to chips? (Yes/No) ")

        if convert_money == "Yes":
            chips_list = chip_table(value_of_chips)
            chips_dict, remaining_money = cashier(value_of_chips)
            display_user_table(chips_dict, remaining_money, value_of_chips)
            break

        elif convert_money == "no":
            print("Okay, maybe next time.")
            break

        else: print("Please answer with 'Yes' or 'No'.")

if __name__ == "__main__":
    main()