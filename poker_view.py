import json
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
data_file = "data.json"

def read_data():
    if os.path.exists(data_file):
        with open(data_file, 'r') as f:
            try:
                data = json.load(f)
                return data
            except json.decoder.JSONDecodeError as e:
                print(f"Errore: Impossibile decodificare il file JSON - {str(e)}")
                # Rimuovi eventuali dati extra e riprova a caricare il file JSON
                f.close()  # Chiudi il file
                with open(data_file, 'w') as f:
                    initial_data = {
                        "value_of_chips": {
                            "white": 1,
                            "red": 5,
                            "blue": 10,
                            "green": 25,
                            "black": 100,
                            "purple": 500,
                            "yellow": 1000,
                            "pink": 5000,
                            "light blue": 10000
                        },
                        "user_chips": {
                            "white": 0,
                            "red": 0,
                            "blue": 0,
                            "green": 0,
                            "black": 0,
                            "purple": 0,
                            "yellow": 0,
                            "pink": 0,
                            "light blue": 0
                        },
                        "total_money": 0,
                        "remaining_money": 0
                    }
                    json.dump(initial_data, f, indent=4)
                    return initial_data
    else:
        return None

def create_or_update_data():
    if not os.path.exists(data_file):
        initial_data = {
            "value_of_chips": {
                "white": 1,
                "red": 5,
                "blue": 10,
                "green": 25,
                "black": 100,
                "purple": 500,
                "yellow": 1000,
                "pink": 5000,
                "light blue": 10000
            },
            "user_chips": {
                "white": 0,
                "red": 0,
                "blue": 0,
                "green": 0,
                "black": 0,
                "purple": 0,
                "yellow": 0,
                "pink": 0,
                "light blue": 0
            },
            "total_money": 0,
            "remaining_money": 0
        }
        with open(data_file, 'w') as f:
            json.dump(initial_data, f, indent=4)
    else:
        with open(data_file, 'r+') as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError as e:
                print(f"Errore: Impossibile decodificare il file JSON - {str(e)}")
                return

            if "user_chips" not in data:
                data["user_chips"] = {
                    "white": 0,
                    "red": 0,
                    "blue": 0,
                    "green": 0,
                    "black": 0,
                    "purple": 0,
                    "yellow": 0,
                    "pink": 0,
                    "light blue": 0
                }
                f.seek(0)
                json.dump(data, f, indent=4)

create_or_update_data()

# Funzione per la rotta '/'
@app.route('/')
def welcome():
    return render_template('cover_progect.html')

# Funzione per la rotta '/casino_home'
@app.route('/casino_home')
def casino_home():
    return render_template('casino_home.html')

# Funzione per la rotta '/poker_rules'
@app.route('/poker_rules')
def poker_rules():
    return render_template('poker_rules.html')

# Funzione per la rotta '/home_poker.html'
@app.route('/home_poker.html')
def home_poker():
    return render_template('home_poker.html')

# Funzione per la rotta '/texas_holdem'
@app.route('/texas_holdem', methods=['GET', 'POST'])
def texas_holdem():
    if request.method == 'POST':
        data = read_data()
        if data:
            value_of_chips = data["value_of_chips"]
            return render_template('texas_holdem_game.html', value_of_chips=value_of_chips)
        else:
            return "Errore: Il file JSON non esiste."
    else:
        return render_template('texas_holdem.html')

# Funzione per la rotta '/play'
@app.route('/play', methods=['GET', 'POST'])
def play():
    if request.method == 'POST':
        data = read_data()
        if data:
            value_of_chips = data["value_of_chips"]
            return render_template('generic_game.html', value_of_chips=value_of_chips)
        else:
            return "Errore: Il file JSON non esiste."
    else:
        return render_template('play.html')

# Funzione per la rotta '/cashier'
@app.route('/cashier', methods=['GET', 'POST'])
def cashier_page():
    create_or_update_data()
    data = read_data()
    if data:
        value_of_chips = data.get("value_of_chips", {})  
        total_money = data.get("total_money", 0)  
        remaining_money = data.get("remaining_money", 0)  

        if request.method == 'POST':
            new_total_money_str = request.form.get('total_money', '')
            if new_total_money_str.strip():
                new_total_money = int(new_total_money_str)
            else:
                new_total_money = 0

            difference = new_total_money - total_money
            data["remaining_money"] += difference
            data["total_money"] = new_total_money
            try:
                with open(data_file, "w") as f:
                    json.dump(data, f, indent=4)
                return redirect(url_for('user_dashboard'))
            except json.decoder.JSONDecodeError as e:
                return f"Errore: Impossibile decodificare il file JSON - {str(e)}"
        else:
            return render_template('cashier_operations.html', value_of_chips=value_of_chips, total_money=total_money, remaining_money=remaining_money)
    else:
        return "Errore: Il file JSON non esiste."

# Funzione per la rotta '/convert_to_chips'
@app.route('/convert_to_chips', methods=['POST'])
def convert_to_chips():
    data = read_data()
    if data:
        value_of_chips = data["value_of_chips"]
        amount = int(request.form['amount'])
        chip_color = request.form['chip-color']
        remaining_money = data.get("remaining_money", 0)
        chip_value = value_of_chips.get(chip_color, 0)
        
        # Verifica se il colore del chip è valido
        if chip_color not in value_of_chips:
            return "Errore: Colore del chip non valido."
        
        # Verifica se l'utente ha abbastanza soldi per convertire i chip
        if amount * chip_value > remaining_money:
            return "Errore: Fondi insufficienti per convertire questi chip."
        
        # Calcola quanti chip possono essere convertiti
        quantity = amount
        
        # Aggiorna i dati relativi ai chip e ai soldi rimanenti
        data["remaining_money"] -= quantity * chip_value
        data["user_chips"][chip_color] += quantity
        
        # Aggiorna il file JSON
        try:
            with open(data_file, "w") as f:
                json.dump(data, f, indent=4)
            return redirect(url_for('user_dashboard'))
        except json.decoder.JSONDecodeError as e:
            return f"Errore: Impossibile decodificare il file JSON - {str(e)}"
    else:
        return "Errore: Il file JSON non esiste."

# Funzione per la rotta '/convert_to_money'
@app.route('/convert_to_money', methods=['POST'])
def convert_to_money():
    data = read_data()
    if data:
        value_of_chips = data["value_of_chips"]
        chip_color = request.form['chip-color']
        quantity = int(request.form['quantity'])
        chip_value = value_of_chips.get(chip_color, 0)
        amount = quantity * chip_value
        remaining_money = data.get("remaining_money", 0)
        
        # Calcoliamo il denaro necessario per le fiches richieste
        money_needed = amount
        
        # Verifichiamo se ci sono fondi sufficienti per la conversione
        if money_needed > remaining_money:
            return "Errore: Fondi insufficienti per convertire queste chip."
        
        # Aggiorniamo i dati relativi ai soldi rimanenti e al saldo totale
        data["remaining_money"] -= money_needed
        data["total_money"] += money_needed
        
        # Aggiorniamo il file JSON
        try:
            with open(data_file, "w") as f:
                json.dump(data, f, indent=4)
            return redirect(url_for('user_dashboard'))
        except json.decoder.JSONDecodeError as e:
            return f"Errore: Impossibile decodificare il file JSON - {str(e)}"
    else:
        return "Errore: Il file JSON non esiste."

# Funzione per la rotta '/reconvert'
@app.route('/reconvert', methods=['POST'])
def reconvert():
    data = read_data()
    if data:
        value_of_chips = data["value_of_chips"]
        chips_dict = {request.form['chip-color']: int(request.form['quantity'])}
        total_money = convert_back(chips_dict, value_of_chips)
        return render_template('reconvert.html', total_money=total_money)
    else:
        return "Errore: Il file JSON non esiste."

def convert_back(chips_dict, value_of_chips):
    """This function converts chips back to money"""
    total_money = 0
    for color, number in chips_dict.items():
        chip_value = int(value_of_chips[color])
        total_money += number * chip_value  # Qui abbiamo corretto la moltiplicazione
    return total_money

# Funzione per la rotta '/user_dashboard'
@app.route('/user_dashboard')
def user_dashboard():
    data = read_data()
    if data:
        user_chips = data["user_chips"]
        total_money = data["total_money"]
        remaining_money = data["remaining_money"]
        value_of_chips = data["value_of_chips"]
        return render_template('user_dashboard.html', user_chips=user_chips, total_money=total_money, remaining_money=remaining_money, value_of_chips=value_of_chips)
    else:
        return "Errore: Il file JSON non esiste."

# Funzione per la rotta '/update_total_money'
@app.route('/update_total_money', methods=['POST'])
def update_total_money():
    if request.method == 'POST':
        new_total_money = int(request.form.get('total_money', 0))
        data = read_data()
        if data:
            data["total_money"] = new_total_money
            try:
                with open(data_file, "w") as f:
                    json.dump(data, f, indent=4)
                return redirect(url_for('user_dashboard'))
            except json.decoder.JSONDecodeError as e:
                return f"Errore: Impossibile decodificare il file JSON - {str(e)}"
        else:
            return "Errore: Il file JSON non esiste."
    else:
        return "Metodo non consentito."

# Funzione per la rotta '/clear_user_data'
@app.route('/clear_user_data', methods=['POST'])
def clear_user_data():
    create_or_update_data()
    return redirect(url_for('user_dashboard'))

# Funzione per la rotta '/clear_cashier_data'
@app.route('/clear_cashier_data', methods=['POST'])
def clear_cashier_data():
    create_or_update_data()
    return redirect(url_for('cashier_page'))

# Funzione per la rotta '/clear_all_data'
@app.route('/clear_all_data', methods=['POST'])
def clear_all_data():
    create_or_update_data()
    if os.path.exists(data_file):
        try:
            with open(data_file, 'r+') as f:
                data = json.load(f)
                data["user_chips"] = {
                    "white": 0,
                    "red": 0,
                    "blue": 0,
                    "green": 0,
                    "black": 0,
                    "purple": 0,
                    "yellow": 0,
                    "pink": 0,
                    "light blue": 0
                }
                data["total_money"] = 0
                data["remaining_money"] = 0
                f.seek(0)
                json.dump(data, f, indent=4)
            return redirect(url_for('cashier_page'))
        except json.decoder.JSONDecodeError as e:
            return f"Errore: Impossibile decodificare il file JSON - {str(e)}"
    else:
        create_or_update_data()
        return redirect(url_for('cashier_page'))

if __name__ == '__main__':
    app.run(debug=True, port=12345)