import os
import json
from Funzionamento_del_Poker import deck_creation, deck_shuffle

def main():
    # Dati per creare il mazzo
    seeds = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values_of_cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    # Creazione del mazzo
    deck = deck_creation(seeds, values_of_cards)

    # Mischia il mazzo
    shuffled_deck = deck_shuffle(deck)

    # Inizializza il dizionario per il mazzo organizzato
    organized_deck = initialize_organized_deck(seeds)

    # Ordina le carte per seme e valore
    for card in shuffled_deck:
        seed = card["seed"]
        value = card["value"]
        organized_deck[seed].append({"value": value})

    # Ordina le carte all'interno di ciascun seme per valore
    for seed in organized_deck:
        organized_deck[seed] = sorted(organized_deck[seed], key=lambda x: values_of_cards.index(x["value"]))

    # Nome del file JSON
    file_name = 'deck_into_json.json'

    # Scrive il mazzo mischiato in un file JSON
    with open(file_name, 'w') as json_file:
        json.dump(organized_deck, json_file, indent=4)
        print(f"Il mazzo è stato salvato in '{file_name}'")

def initialize_organized_deck(seeds):
    return {seed: [] for seed in seeds}

if __name__ == "__main__":
    main()