from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():

    # Assegnazione delle carte
    user_cards = ["01_spades.png", "13_hearts.png"]  # L'utente ha l'asso di picche e il re di cuori
    dealer_cards = ["05_clubs.png", "11_diamonds.png"]  # Il dealer ha il 5 di fiori e il fante di quadri
    community_cards = ["07_diamonds.png", "08_spades.png", "09_hearts.png", "11_hearts.png", "12_diamonds.png"]  # Le carte comunitarie
    
    # Rendering del template HTML
    return render_template('poker.html', user_cards=user_cards, dealer_cards=dealer_cards, community_cards=community_cards)

if __name__ == '__main__':
    app.run(debug=True) 