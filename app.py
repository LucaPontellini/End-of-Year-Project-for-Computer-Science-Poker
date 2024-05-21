from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():

    # Assegnazione delle carte
    user_cards = ["https://github.com/LucaPontellini/End-of-Year-Project-for-Computer-Science-Poker-/blob/main/static/foto_delle_carte/quadri/04_diamonds.png", "KH.png"]  # L'utente ha l'asso di picche e il re di cuori
    dealer_cards = ["5C.png", "JD.png"]  # Il dealer ha il 5 di fiori e il fante di quadri
    community_cards = ["7D.png", "8S.png", "9H.png", "TC.png", "QD.png"]  # Le carte comunitarie
    
    # Rendering del template HTML
    return render_template('poker.html', user_cards=user_cards, dealer_cards=dealer_cards, community_cards=community_cards)

if __name__ == '__main__':
    app.run(debug=True)