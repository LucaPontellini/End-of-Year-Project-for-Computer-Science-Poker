from flask import Flask, render_template
import random

app = Flask(__name__)


def get_random_card(suit):
    return f"{suit}/{random.randint(1, 13):02d}_{suit}.png"

@app.route('/')
def index():
    card_images_folder = 'foto_delle_carte'
    suits = ['hearts', 'diamonds', 'clubs', 'spades']

    user_cards = [f"{card_images_folder}/{get_random_card(random.choice(suits))}" for _ in range(2)]
    dealer_cards = [f"{card_images_folder}/{get_random_card(random.choice(suits))}" for _ in range(2)]
    community_cards = [f"{card_images_folder}/{get_random_card(random.choice(suits))}" for _ in range(5)]

    return render_template('poker.html', user_cards=user_cards, dealer_cards=dealer_cards, community_cards=community_cards)

if __name__ == '__main__':
    app.run(debug=True)