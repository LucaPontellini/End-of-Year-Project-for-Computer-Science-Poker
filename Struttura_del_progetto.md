## Struttura del progetto

La struttura del progetto 

```text
End-of-Year-Project-for-Computer-Science-Poker/
│   
├── static/                                     #        
│   ├── cover_project.css                       #              
│   ├── styles.css                              #
│   ├── styles_1.css                            #
│   │
│   ├── cashier.jpg                             #
│   ├── cassiere.webp                           #
│   ├── immagine_Casino.jpg                     #
│   ├── interno_Casinò.jpg                      #
│   ├── mano_con_le_carte.jpg                   #
│   ├── tavolo_poker_con_mano.png               #
│   ├── tavolo_poker.jpg                        #   
│   ├── tavolo_Texas_Holdem.jpg                 #
│   │ 
│   ├── foto_dei_giochi_del_Casinò/             #              
│   │   ├── blackjack.jpg                       #
│   │   ├── caribbean stud poker.jpg            #
│   │   ├── crabs.jpg                           #
│   │   ├── poker texas holdem.jpg              #
│   │   ├── roulette.jpg                        #
│   │   ├── slot machine.jpg                    #
│   │   └── video poker.jpg                     #
│   │
│   ├── foto_delle_carte/                       #
│   │   ├── hearts/                             #
│   │   │   ├── 01_hearts.png                   #
│   │   │   ├── 02_hearts.png                   #
│   │   │   ├── 03_hearts.png                   #
│   │   │   ├── 04_hearts.png                   #
│   │   │   ├── 05_hearts.png                   #
│   │   │   ├── 06_hearts.png                   #
│   │   │   ├── 07_hearts.png                   #
│   │   │   ├── 08_hearts.png                   #
│   │   │   ├── 09_hearts.png                   #
│   │   │   ├── 10_hearts.png                   #
│   │   │   ├── 11_hearts.png                   #
│   │   │   ├── 12_hearts.png                   #
│   │   │   └── 13_hearts.png                   #
│   │   │                   
│   │   ├── diamonds/
│   │   │   ├── 01_diamonds.png                 #
│   │   │   ├── 02_diamonds.png                 #
│   │   │   ├── 03_diamonds.png                 #
│   │   │   ├── 04_diamonds.png                 #
│   │   │   ├── 05_diamonds.png                 #
│   │   │   ├── 06_diamonds.png                 #
│   │   │   ├── 07_diamonds.png                 #
│   │   │   ├── 08_diamonds.png                 #
│   │   │   ├── 09_diamonds.png                 #
│   │   │   ├── 10_diamonds.png                 #
│   │   │   ├── 11_diamonds.png                 #
│   │   │   ├── 12_diamonds.png                 #
│   │   │   └── 13_diamonds.png                 #
│   │   │ 
│   │   ├── clubs/
│   │   │   ├── 01_clubs.png                    #
│   │   │   ├── 02_clubs.png                    #
│   │   │   ├── 03_clubs.png                    #
│   │   │   ├── 04_clubs.png                    #
│   │   │   ├── 05_clubs.png                    #
│   │   │   ├── 06_clubs.png                    #
│   │   │   ├── 07_clubs.png                    #
│   │   │   ├── 08_clubs.png                    #
│   │   │   ├── 09_clubs.png                    #
│   │   │   ├── 10_clubs.png                    #
│   │   │   ├── 11_clubs.png                    #
│   │   │   ├── 12_clubs.png                    #
│   │   │   └── 13_clubs.png                    #
│   │   │
│   │   └── spades/
│   │       ├── 01_spades.png                   #
│   │       ├── 02_spades.png                   #
│   │       ├── 03_spades.png                   #
│   │       ├── 04_spades.png                   #
│   │       ├── 05_spades.png                   #
│   │       ├── 06_spades.png                   #
│   │       ├── 07_spades.png                   #
│   │       ├── 08_spades.png                   #
│   │       ├── 09_spades.png                   #
│   │       ├── 10_spades.png                   #
│   │       ├── 11_spades.png                   #
│   │       ├── 12_spades.png                   #
│   │       └── 13_spades.png                   #
│   │
│   └── Musica_per_il_Poker/                    #   
│       ├── Invisible Cities.mp3                #
│       ├── Jazzy Smile.mp3                     #
│       ├── Two Cigarettes, Please.mp3          #
│       ├── Welcome to New Orleans.mp3          #
│       │
│       ├── invisible-cities.zip                #
│       ├── jazzy-smile.zip                     #
│       ├── two-cigarettes-please.zip           #
│       └── welcome-to-new-orleans.zip          #
│   
├── templates/                                  #
│   ├── data.py                                 #
│   ├── deck_into_json.py                       #
│   ├── Funzionamento_del_Poker.py              #
│   ├── game.py                                 #
│   │
│   ├── data.json                               #
│   │
│   ├── cashier_operations.html                 #
│   ├── casino_home.html                        #
│   ├── cover_progect.html                      #
│   ├── home_poker.html                         #
│   ├── play.html                               #
│   ├── poker_rules.html                        #
│   ├── poker.html                              #
│   ├── return_to_casino_home.html              #
│   ├── return_to_cover_project.html            #
│   └── user_dashboard.html                     #
│
├── stiles.css                                  #
│
├── app.py                                      #
│
├── casino.py                                   #
│
├── IA.py                                       #
│
├── Regole_del_Poker.py                         #
│
├── requirements.txt                            # Gestione Dipendenze
│                                               # - Flask: Il framework core per il web serving e il routing.
│                                               # - Tabulate: 
│                                               
├── LICENSE                                     # Licenza MIT: Uso libero, obbligo di citazione
│                                               # - Garantisce il mio copyright.
│                                               # - Permette a chiunque di usare, copiare e modificare il codice.
│                                               # - Esclude la responsabilità (Disclaimer "AS IS").
│
├── .gitignore                                  # 
│
├── README.md                                   #                                  
│                                  
├── poker.ipynb                                 # 
│
├── data.json                                   #
│
├── deck_into_json.json                         #
│
├── Appunti per il Poker.docx                   #
│
└── Struttura_del_progetto.md                   #
```