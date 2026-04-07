## Struttura del progetto:

La seguente struttura rappresenta l’organizzazione attuale del progetto End-of-Year-Project-for-Computer-Science-Poker.
La struttura è stata progettata per essere funzionale, ma presenta alcune aree di disorganizzazione che potrebbero essere migliorate in futuro. 
Inoltre, oltre alle criticità già presenti nel codice, l’intero progetto presenta una significativa incoerenza nella nomenclatura dei file: alcuni sono in italiano, altri in inglese, e in diversi casi le due lingue vengono mescolate. 
Questa mancanza di uniformità linguistica rende più difficile orientarsi nella struttura e compromette la leggibilità complessiva del progetto.

```text
End-of-Year-Project-for-Computer-Science-Poker/
│   
├── static/                                     # Contiene tutte le risorse statiche come immagini, stili CSS e musica.
│   ├── cover_project.css                       # Stile grafico della pagina di copertina: sfondo del casinò, pulsante Play e box informativi.             
│   ├── styles.css                              # Foglio di stile principale: gestisce sfondi, layout delle sezioni, pulsanti, container e tema grafico del casinò.
│   ├── styles_1.css                            # Stili dedicati alla disposizione delle carte: posizionamento di player, dealer e community cards sul tavolo.
│   │
│   ├── cashier.jpg                             # Immagine di sfondo della pagina del cassiere.
│   ├── cassiere.webp                           # Placeholder per la pagina del cassiere.
│   ├── immagine_Casino.jpg                     # Immagine per la pagina di copertina del progetto.
│   ├── interno_Casinò.jpg                      # Immagine di sfondo per la pagina principale del casinò.
│   ├── mano_con_le_carte.jpg                   # Immagine predisposta per ospitare le carte del player in fase di gioco (placeholder).
│   ├── tavolo_poker_con_mano.png               # Immagine del tavolo da Poker con la mano del player utilizzata come sfondo per la pagina di gioco.
│   ├── tavolo_poker.jpg                        # Immagine di presentazione del Poker pre-pagina delle regole di gioco. 
│   ├── tavolo_Texas_Holdem.jpg                 # Immagine del tavolo da gico senza mano del player, utilizzata come sfondo della partita di gioco del Texas Hold'em.
│   │ 
│   ├── foto_dei_giochi_del_Casinò/             # Contiene le immagini dei giochi del casinò utilizzate come placeholder per la lobby del casinò.              
│   │   ├── blackjack.jpg                       # Placeholder per il gioco del blackjack.
│   │   ├── caribbean stud poker.jpg            # Placeholder per il gioco del Caribbean Stud Poker.
│   │   ├── crabs.jpg                           # Placeholder per il gioco dei crabs.
│   │   ├── poker texas holdem.jpg              # Placeholder per il gioco del poker texas holdem.
│   │   ├── roulette.jpg                        # Placeholder per il gioco della roulette.
│   │   ├── slot machine.jpg                    # Placeholder per il gioco delle slot machine.
│   │   └── video poker.jpg                     # Placeholder per il gioco del video poker.
│   │
│   ├── foto_delle_carte/                       # Contiene le immagini di tutte le carte da gioco riutilizzabili per ogni gioco di carte del casinò.
│   │   ├── hearts/                             # Contiene le immagini delle carte di cuori, numerate da 1 a 13 (Asso, 2-10, Jack, Regina, Re).
│   │   │   ├── 01_hearts.png                   # Immagine dell'Asso di cuori.
│   │   │   ├── 02_hearts.png                   # Immagine del 2 di cuori.
│   │   │   ├── 03_hearts.png                   # Immagine del 3 di cuori.
│   │   │   ├── 04_hearts.png                   # Immagine del 4 di cuori.
│   │   │   ├── 05_hearts.png                   # Immagine del 5 di cuori.
│   │   │   ├── 06_hearts.png                   # Immagine del 6 di cuori.
│   │   │   ├── 07_hearts.png                   # Immagine del 7 di cuori.
│   │   │   ├── 08_hearts.png                   # Immagine del 8 di cuori.
│   │   │   ├── 09_hearts.png                   # Immagine del 9 di cuori.
│   │   │   ├── 10_hearts.png                   # Immagine del 10 di cuori.
│   │   │   ├── 11_hearts.png                   # Immagine del Jack di cuori.
│   │   │   ├── 12_hearts.png                   # Immagine della Regina di cuori.
│   │   │   └── 13_hearts.png                   # Immagine del Re di cuori.
│   │   │                   
│   │   ├── diamonds/                           # Contiene le immagini delle carte di quadri, numerate da 1 a 13 (Asso, 2-10, Jack, Regina, Re). 
│   │   │   ├── 01_diamonds.png                 # Immagine dell'Asso di quadri. 
│   │   │   ├── 02_diamonds.png                 # Immagine del 2 di quadri. 
│   │   │   ├── 03_diamonds.png                 # Immagine del 3 di quadri. 
│   │   │   ├── 04_diamonds.png                 # Immagine del 4 di quadri. 
│   │   │   ├── 05_diamonds.png                 # Immagine del 5 di quadri. 
│   │   │   ├── 06_diamonds.png                 # Immagine del 6 di quadri. 
│   │   │   ├── 07_diamonds.png                 # Immagine del 7 di quadri. 
│   │   │   ├── 08_diamonds.png                 # Immagine del 8 di quadri. 
│   │   │   ├── 09_diamonds.png                 # Immagine del 9 di quadri. 
│   │   │   ├── 10_diamonds.png                 # Immagine del 10 di quadri. 
│   │   │   ├── 11_diamonds.png                 # Immagine del Jack di quadri. 
│   │   │   ├── 12_diamonds.png                 # Immagine della Regina di quadri. 
│   │   │   └── 13_diamonds.png                 # Immagine del Re di quadri. 
│   │   │ 
│   │   ├── clubs/                              # Contiene le immagini delle carte di fiori, numerate da 1 a 13 (Asso, 2-10, Jack, Regina, Re).
│   │   │   ├── 01_clubs.png                    # Immagine dell'Asso di fiori.
│   │   │   ├── 02_clubs.png                    # Immagine del 2 di fiori.
│   │   │   ├── 03_clubs.png                    # Immagine del 3 di fiori.
│   │   │   ├── 04_clubs.png                    # Immagine del 4 di fiori.
│   │   │   ├── 05_clubs.png                    # Immagine del 5 di fiori.
│   │   │   ├── 06_clubs.png                    # Immagine del 6 di fiori.
│   │   │   ├── 07_clubs.png                    # Immagine del 7 di fiori.
│   │   │   ├── 08_clubs.png                    # Immagine del 8 di fiori.
│   │   │   ├── 09_clubs.png                    # Immagine del 9 di fiori.
│   │   │   ├── 10_clubs.png                    # Immagine del 10 di fiori.
│   │   │   ├── 11_clubs.png                    # Immagine del Jack di fiori.
│   │   │   ├── 12_clubs.png                    # Immagine della Regina di fiori.
│   │   │   └── 13_clubs.png                    # Immagine del Re di fiori.
│   │   │
│   │   └── spades/                             # Contiene le immagini delle carte di picche, numerate da 1 a 13 (Asso, 2-10, Jack, Regina, Re).
│   │       ├── 01_spades.png                   # Immagine dell'Asso di picche.
│   │       ├── 02_spades.png                   # Immagine del 2 di picche.
│   │       ├── 03_spades.png                   # Immagine del 3 di picche.
│   │       ├── 04_spades.png                   # Immagine del 4 di picche.
│   │       ├── 05_spades.png                   # Immagine del 5 di picche.
│   │       ├── 06_spades.png                   # Immagine del 6 di picche.
│   │       ├── 07_spades.png                   # Immagine del 7 di picche.
│   │       ├── 08_spades.png                   # Immagine del 8 di picche.
│   │       ├── 09_spades.png                   # Immagine del 9 di picche.
│   │       ├── 10_spades.png                   # Immagine del 10 di picche.
│   │       ├── 11_spades.png                   # Immagine del Jack di picche.
│   │       ├── 12_spades.png                   # Immagine della Regina di picche.
│   │       └── 13_spades.png                   # Immagine del Re di picche.
│   │
│   └── Musica_per_il_Poker/                    # Contiene i file audio utilizzati come sottofondo musicale per le pagine del casinò e del poker, 
│       │                                         oltre a versioni compresse in formato ZIP. 
│       ├── Invisible Cities.mp3                # Sottofondo musicale per la pagina di copertina del progetto, con un'atmosfera misteriosa e coinvolgente.
│       ├── Jazzy Smile.mp3                     # Sottofondo musicale per la pagina principale del casinò, con un ritmo rilassante e sofisticato che richiama l'atmosfera 
│       │                                         di un casinò elegante.
│       ├── Two Cigarettes, Please.mp3          # Sottofondo musicale per la pagina di gioco del poker, con un ritmo più vivace e dinamico che accompagna l'azione del gioco.
│       ├── Welcome to New Orleans.mp3          # Sottofondo musicale per la pagina di gioco del poker, con un ritmo allegro e festoso che richiama l'atmosfera di New Orleans, 
│       │                                         famosa per il suo legame con il poker e i casinò.
│       │
│       ├── invisible-cities.zip                # Versione compressa del file Invisible Cities.mp3, utilizzata per facilitare il download e la gestione dei file audio.
│       ├── jazzy-smile.zip                     # Versione compressa del file Jazzy Smile.mp3, utilizzata per facilitare il download e la gestione dei file audio.
│       ├── two-cigarettes-please.zip           # Versione compressa del file Two Cigarettes, Please.mp3, utilizzata per facilitare il download e la gestione dei file audio.
│       └── welcome-to-new-orleans.zip          # Versione compressa del file Welcome to New Orleans.mp3, utilizzata per facilitare il download e la gestione dei file audio.
│   
├── templates/                                  # Contiene tutti i file HTML, Python e JSON utilizzati per il rendering delle pagine web e la logica di gioco del progetto.
│   ├── data.py                                 # Gestisce la creazione e validazione del file data.json: valori delle fiches, inizializzazione e aggiornamento dei dati del
│   │                                             casinò.
│   ├── deck_into_json.py                       # Genera un mazzo di carte mischiato e lo salva in deck_into_json.json, organizzando le carte per seme e valore
│   ├── Funzionamento_del_Poker.py              # Modulo centrale del gioco: crea e mischia il mazzo, genera carte casuali, gestisce fiches, conversioni e tabelle.  
│   ├── game.py                                 # Modulo completo del gioco: gestisce fiches, azioni di puntata, distribuzione delle carte, classificazione delle mani e
│   │                                             determinazione del vincitore.
│   │
│   ├── data.json                               # Archivio dei dati economici del casinò: valori delle fiches, fiches dell’utente, riconversioni e stato del denaro.
│   │
│   ├── cashier_operations.html                 # Interfaccia del cassiere: mostra valori delle fiches, gestisce conversioni denaro↔fiches, aggiornamenti e reset dei dati con
│   │                                             musica di sottofondo.
│   ├── casino_home.html                        # Home del casinò: mostra i giochi disponibili, gestisce la navigazione verso il poker e il cassiere, con musica di sottofondo e │   │                                             layout a griglia.
│   ├── cover_progect.html                      # Pagina di copertina del casinò: titolo, pulsante Play, link ai profili del creatore e musica di sottofondo.
│   ├── home_poker.html                         # Pagina introduttiva del Texas Hold'em: sfondo dedicato, pulsante per avviare la partita e link alle regole del poker.
│   ├── play.html                               # Pagina di gioco del Texas Hold'em: mostra carte di giocatore, dealer e community con layout posizionale e musica dinamica di │   │                                             sottofondo.
│   ├── poker_rules.html                        # Pagina delle regole del Texas Hold'em: spiega valori delle carte, ranking delle mani, fasi di gioco e include immagini di 
│   │                                             tutte le carte.
│   ├── poker.html                              # Visualizzazione base delle carte: mostra le carte di giocatore, dealer e community su sfondo del tavolo da poker.
│   ├── return_to_casino_home.html              # Versione di ritorno della home del casinò: ripristina la musica, mostra i giochi e reindirizza correttamente dopo il back del
│   │                                             browser.
│   ├── return_to_cover_project.html            # Versione di ritorno della cover: ripristina la musica, mostra titolo e pulsante Play, e mantiene i link ai profili del creatore
│   └── user_dashboard.html                     # Dashboard utente: mostra quantità e valore delle fiches possedute, denaro totale e rimanente, con pulsanti per tornare al 
│                                                 cassiere o riconvertire le fiches.
├── stiles.css                                  # Stili per la disposizione delle carte nel Texas Hold'em: posizionamento di player, dealer e community e dimensioni delle carte.
│
├── app.py                                      # Mini-app Flask di test: genera carte casuali per giocatore, dealer e community e le mostra tramite poker.html
│
├── casino.py                                   # Applicazione Flask principale: gestisce routing del casinò, caricamento e aggiornamento dei dati JSON, operazioni del 
│                                                 cassiere, generazione delle carte e logica di gioco.
├── IA.py                                       # Logica dell’IA del dealer: valuta la mano, decide puntate/check/fold e gestisce il turno del giocatore con input testuale (la 
│                                                 logica è sbagliata perchè il dealer non deve giocare, ma fare solo le sue funzioni).
├── Regole_del_Poker.py                         # Motore logico del poker: riconoscimento delle mani, distribuzione carte, azioni di gioco (check/bet/fold) e determinazione del 
│                                                 vincitore.
├── requirements.txt                            # Gestione Dipendenze
│                                               # - Flask: Il framework core per il web serving e il routing.
│                                               # - Tabulate: Utilizzato per formattare e visualizzare le tabelle dei dati in modo leggibile, soprattutto per il terminale.
│                                               
├── LICENSE                                     # Licenza MIT: Uso libero, obbligo di citazione
│                                               # - Garantisce il mio copyright.
│                                               # - Permette a chiunque di usare, copiare e modificare il codice.
│                                               # - Esclude la responsabilità (Disclaimer "AS IS").
│
├── .gitignore                                  # Esclude file e cartelle non necessari dal controllo di versione, come __pycache__, file temporanei, dati sensibili, ecc.
│
├── README.md                                   # Contiene una panoramica del progetto, istruzioni per l'installazione e l'uso, e informazioni sullo sviluppo 
│                                                 futuro.                                  
│                                  
├── poker.ipynb                                 # Notebook di sviluppo: contiene codice di test, esperimenti e prototipi per la logica del poker, l'IA e la gestione dei dati.
│
├── data.json                                   # Archivio persistente del casinò: contiene valori delle fiches, fiches dell’utente, denaro totale e rimanente, aggiornati dal 
│                                                 cashier.
├── deck_into_json.json                         # Mazzo di carte completo organizzato per seme e valore, generato e salvato all’avvio dell’app per l’uso nelle funzioni di gioco.
│
├── Appunti per il Poker.docx                   # Lista delle funzionalità che dovrebbero essere state implementate per completare il sistema di Poker nel progetto del Casinò 
│                                                 nei tempi previsti, ma che non sono mai state realizzate a causa di problemi di tempo, organizzazione e gestione del progetto. 
│
└── Struttura_del_progetto.md                   # File più recente del progetto, che funge da panoramica dettagliata della struttura del progetto, con le caratteristiche di 
                                                  ogni elemento del progetto, e una riflessione sulle aree di disorganizzazione e miglioramento.
```