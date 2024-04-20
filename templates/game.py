import os
import random
import json
from tabulate import tabulate
from Funzionamento_del_Poker import deck_creation, deck_shuffle, draw_card
from data import value_of_chips

# Funzioni per la creazione del mazzo e le operazioni sui chip

def chip_table(value_of_chips):
    """This feature creates and prints a poker chip table"""
    chips_list = []
    for color, value in value_of_chips.items():
        chips_list.append([color, value])

    print(tabulate(chips_list, headers=['Color', 'Value'], tablefmt='grid'))
    return chips_list

def cashier(value_of_chips):
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
            else: 
                print("You don't have enough money for that many chips. Please enter a smaller number.")

    print(tabulate([[color, number] for color, number in chips_dict.items()], headers=['Color', 'Number'], tablefmt='grid'))
    print(f"You have ${remaining_money} remaining.")
    return chips_dict, remaining_money

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

# Funzioni per il gioco

def check():
    """This function represents the 'check' action in poker. When a player checks, they bet nothing"""
    print("Player checks.")
    pass

def bet(chips):
    """This function represents the 'bet' action in poker. When a player bets, they wager a certain number of chips"""
    print(f"Player bets {chips} chips.")
    return chips

def call(amount):
    """This function represents the 'call' action in poker. When a player calls, they match another player's bet"""
    print(f"Player calls with {amount}.")
    return amount

def raise_bet(initial_amount, raise_amount):
    """This function represents the 'raise' action in poker. When a player raises, they increase the bet"""
    print(f"Player raises. The bet increases from {initial_amount} to {initial_amount + raise_amount}.")
    return initial_amount + raise_amount

def fold():
    """This function represents the 'fold' action in poker. When a player folds, they forfeit the hand"""
    print("Player folds.")
    pass

# Funzioni per la classificazione delle mani

def pair(hand):
    """Check if a hand has a pair"""
    values = []
    for card in hand:
        values.append(card['value'])

    has_pair = False
    for value in values:
        if values.count(value) == 2:
            has_pair = True
            break

    return has_pair

def two_pairs(hand):

    """Check if a hand has two different pairs"""

    values = []

    for card in hand:
        values.append(card['value'])

    pairs = []

    for value in values:
        if values.count(value) == 2 and value not in pairs:
            pairs.append(value)

    return len(pairs) == 2

def three_of_a_kind(hand):

    """Check if a hand has three of a kind"""

    values = []

    for card in hand:
        values.append(card['value'])

    has_three_of_a_kind = False

    for value in values:
        if values.count(value) == 3:
            has_three_of_a_kind = True
            break

    return has_three_of_a_kind

def straight(hand):
    
    """Check if a hand has a straight"""

    card_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    values = []

    for card in hand:
        card_value = card['value']
        index = card_values.index(card_value)
        values.append(index)

    values.sort()

    is_straight = True
    for i in range(1, len(values)):
        if values[i] - values[i-1] != 1:
            is_straight = False

    if not is_straight:
        has_ace = False
        for card in hand:
            if card['value'] == 'A':
                has_ace = True

        if has_ace:
            values.remove(12)
            values.append(-1)
            values.sort()

            is_straight = True
            for i in range(1, len(values)):
                if values[i] - values[i-1] != 1:
                    is_straight = False

    return is_straight

def flush(hand):

    """Check if a hand has a flush"""

    suits = []

    for card in hand:
        suits.append(card['seed'])

    is_flush = len(set(suits)) == 1

    return is_flush

def full_house(hand):

    """Check if a hand has a full house"""

    return three_of_a_kind(hand) and pair(hand)

def four_of_a_kind(hand):

    """Check if a hand has four of a kind"""

    values = []

    for card in hand:
        values.append(card['value'])

    has_four_of_a_kind = False

    for value in values:
        if values.count(value) == 4:
            has_four_of_a_kind = True
            break

    return has_four_of_a_kind

def straight_flush(hand):

    """Check if a hand has a straight flush"""

    return straight(hand) and flush(hand)

# Funzioni per la distribuzione delle carte

def distribute_cards(deck):

    """Distribute two hole cards to each player"""

    player_hand = [draw_card(deck), draw_card(deck)]
    dealer_hand = [draw_card(deck), draw_card(deck)]

    return player_hand, dealer_hand

def flop(deck):

    """Distribute the flop"""

    return [draw_card(deck), draw_card(deck), draw_card(deck)]

def turn(deck):

    """Distribute the turn card"""

    return draw_card(deck)

def river(deck):

    """Distribute the river card"""

    return draw_card(deck)

# Funzioni per determinare il vincitore

def show_cards(player_hand, dealer_hand):

    """Show all cards"""

    print("Player's cards: ", player_hand)
    print("Dealer's cards: ", dealer_hand)

hand_rankings = {straight_flush: 9,
                 four_of_a_kind: 8,
                 full_house: 7, 
                 flush: 6,
                 straight: 5,
                 three_of_a_kind: 4, 
                 two_pairs: 3,
                 pair: 2
                }

def determine_winner(player_hand, dealer_hand):

    """Determine the winner"""
    
    player_ranking = 1
    for check_hand, ranking in hand_rankings.items():
        if check_hand(player_hand):
            player_ranking = ranking
            break

    dealer_ranking = 1
    for check_hand, ranking in hand_rankings.items():
        if check_hand(dealer_hand):
            dealer_ranking = ranking
            break

    if player_ranking > dealer_ranking:
        return "Player wins!"
    elif dealer_ranking > player_ranking:
        return "Dealer wins!"
    else:
        return "It's a tie!"

# Funzioni per il salvataggio e il caricamento dei dati

def verifica_file_json(nome_file, fiches):
    if os.path.exists(nome_file):
        print(f"Il file '{nome_file}' esiste.")
        try:
            with open(nome_file, 'r') as f:
                data = json.load(f)
                print(f"Il file '{nome_file}' contiene dati JSON validi.")
                return data
        except json.JSONDecodeError as e:
            print(f"Errore nel caricamento dei dati JSON dal file '{nome_file}': {e}")
            print(f"Creazione di un nuovo file JSON valido...")
    else:
        print(f"Il file '{nome_file}' non esiste.")
        print(f"Creazione del file '{nome_file}' con i dati iniziali...")
    with open(nome_file, 'w') as f:
        fiches_without_dollar = {color: int(value) for color, value in fiches.items()}
        json.dump({"value_of_chips": fiches_without_dollar, "total_money": 0, "remaining_money": 0}, f, indent=4)
    return {"value_of_chips": fiches, "total_money": 0, "remaining_money": 0}

def aggiungi_fiches_al_json(nome_file_json, fiches):
    data = verifica_file_json(nome_file_json, value_of_chips)
    if data:
        data["value_of_chips"] = {color: int(value) for color, value in fiches.items()}
        with open(nome_file_json, 'w') as f:
            json.dump(data, f, indent=4)
            print(f"Le fiches sono state aggiornate nel file '{nome_file_json}'.")

def initialize_organized_deck(seeds):
    return {seed: [] for seed in seeds}

# Funzione main

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

        if convert_money.lower() == "yes":
            chips_list = chip_table(value_of_chips)
            chips_dict, remaining_money = cashier(value_of_chips)
            display_user_table(chips_dict, remaining_money, value_of_chips)
            break

        elif convert_money.lower() == "no":
            print("Okay, maybe next time.")
            break

        else: 
            print("Please answer with 'Yes' or 'No'.")

    # Distribuzione delle carte
    player_hand, dealer_hand = distribute_cards(deck)

    # Fase di scommesse (pre-flop)
    # Qui dovresti implementare la logica per gestire le scommesse dei giocatori

    # Flop
    table_cards = flop(deck)
    print("Flop:", table_cards)

    # Fase di scommesse (post-flop)
    # Qui dovresti implementare la logica per gestire le scommesse dei giocatori dopo il flop

    # Turn
    table_cards.append(turn(deck))
    print("Turn:", table_cards)

    # Fase di scommesse (post-turn)
    # Qui dovresti implementare la logica per gestire le scommesse dei giocatori dopo il turn

    # River
    table_cards.append(river(deck))
    print("River:", table_cards)

    # Fase di scommesse (post-river)
    # Qui dovresti implementare la logica per gestire le scommesse dei giocatori dopo il river

    # Determinazione del vincitore
    show_cards(player_hand, dealer_hand)
    winner = determine_winner(player_hand + table_cards, dealer_hand + table_cards)
    print("Winner:", winner)

if __name__ == "__main__":
    main()