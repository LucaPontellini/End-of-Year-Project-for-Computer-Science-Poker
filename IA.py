from Regole_del_Poker import check, bet, fold
from Regole_del_Poker import hand_rankings
from templates.Funzionamento_del_Poker import draw_card, deck_creation, deck_shuffle

def dealer_betting(deck, table_cards, current_bet):
    card1 = draw_card(deck)
    card2 = draw_card(deck)

    hand = [card1, card2] + table_cards

    for check_hand, ranking in hand_rankings.items():
        if check_hand(hand):
            action = bet(ranking)
            current_bet = ranking
            break
    else:
        if current_bet == 0:
            action = check()
        else: 
            action = fold()

    return action, current_bet, [card1, card2]

def player_turn(deck, table_cards, current_bet):
    card1 = draw_card(deck)
    card2 = draw_card(deck)

    hand = [card1, card2] + table_cards

    print("Your cards are: ", hand)
    action = input("Do you want to 'check', 'bet', or 'fold'? ")

    if action == 'bet':
        bet_amount = int(input("How much do you want to bet? "))
        current_bet += bet_amount

    elif action == 'check':
        pass

    elif action == 'fold':
        return 'fold', current_bet, [card1, card2]
    
    else: 
        print("Action not recognized. Please try again.")

    return action, current_bet, [card1, card2]

def main():

    seeds = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values_of_cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    deck = deck_creation(seeds, values_of_cards)
    deck_shuffle(deck)

    table_cards = []
    current_bet = 0

    dealer_action, current_bet, dealer_cards = dealer_betting(deck, table_cards, current_bet)
    print("Dealer action: ", dealer_action)

    player_action, current_bet, player_cards = player_turn(deck, table_cards, current_bet)
    print("Player action: ", player_action)

if __name__ == "__main__":
    main()