import json
import os

value_of_chips = {
    "white": "1",
    "red": "5",
    "blue": "10",
    "green": "25",
    "black": "100",
    "purple": "500",
    "yellow": "1000",
    "pink": "5000",
    "light blue": "10000"
}

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

nome_file_json = "data.json"

aggiungi_fiches_al_json(nome_file_json, value_of_chips)

with open(nome_file_json, 'r') as f:
    data = json.load(f)
    print("Fiches nel file JSON:")
    print(data["value_of_chips"])