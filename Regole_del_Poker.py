# Valore delle carte:
# Le carte sono classificate in base al loro valore, dall’asso (A) al re (K).
# Le quattro semi sono cuori (♥), quadri (♦), fiori (♣) e picche (♠).

from templates.Funzionamento_del_Poker import deck_creation, deck_shuffle, draw_card
from IA import dealer_betting, player_turn

# Classificazione delle mani:
# Coppia: Due carte dello stesso valore.
# Doppia coppia: Due coppie di carte.
# Tris: Tre carte dello stesso valore.
# Scala: Cinque carte consecutive (ad esempio, 2-3-4-5-6).
# Colore: Cinque carte dello stesso seme.
# Full: Una coppia più un tris.
# Poker: Quattro carte dello stesso valore.
# Scala reale: Scala dall’asso al dieci dello stesso seme.

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

# Distribuzione delle carte:
# Ogni giocatore riceve due carte coperte (le “hole cards”).

def distribute_cards(deck):

    """Distribute two hole cards to each player"""

    player_hand = [draw_card(deck), draw_card(deck)]
    dealer_hand = [draw_card(deck), draw_card(deck)]

    return player_hand, dealer_hand

# Segue una fase di scommesse.
# Scommesse:
# I giocatori possono effettuare diverse azioni:

# Check: Passare il turno senza scommettere.
# Bet: Scommettere una certa quantità di chip.
# Call: Pareggiare la scommessa di un altro giocatore.
# Raise: Aumentare la scommessa.
# Fold: Abbandonare la mano.

def check():

    """This function represents the "check" action in poker. When a player checks, they bet nothing"""

    print("Player checks.")
    pass

def bet(chips):

    """This function represents the "bet" action in poker. When a player bets, they wager a certain number of chips"""

    print(f"Player bets {chips} chips.")
    return chips

def call(amount):

    """This function represents the "call" action in poker. When a player calls, they match another player's bet"""

    print(f"Player calls with {amount}.")
    return amount

def raise_bet(initial_amount, raise_amount):

    """This function represents the "raise" action in poker. When a player raises, they increase the bet"""

    print(f"Player raises. The bet increases from {initial_amount} to {initial_amount + raise_amount}.")
    return initial_amount + raise_amount

def fold():

    """This function represents the "fold" action in poker. When a player folds, they forfeit the hand"""

    print("Player folds.")
    pass

# Vengono distribuite tre carte scoperte sul tavolo (il “flop”).

def flop(deck):

    """Distribute the flop"""

    return [draw_card(deck), draw_card(deck), draw_card(deck)]

# Altre due carte scoperte vengono distribuite una alla volta (il “turn” e il “river”).

def turn(deck):

    """Distribute the turn card"""

    return draw_card(deck)

def river(deck):

    """Distribute the river card"""

    return draw_card(deck)

# I giocatori cercano di formare la migliore mano possibile utilizzando le loro hole cards e le carte comuni sul tavolo.

# Vincitore:
# Alla fine del round di scommesse, i giocatori mostrano le loro carte.
# Vince il giocatore con la mano più alta secondo la classificazione sopra.

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

def main():

    seeds = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values_of_cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    deck = deck_creation(seeds, values_of_cards)
    deck_shuffle(deck)

    table_cards = []
    current_bet = 0

    dealer_action, current_bet, dealer_cards = dealer_betting(deck, table_cards, current_bet)
    print("Azione del dealer: ", dealer_action)

    player_action, current_bet, player_cards = player_turn(deck, table_cards, current_bet)
    print("Azione del giocatore: ", player_action)

if __name__ == "__main__":
    main()