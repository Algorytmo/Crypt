# Crypt
Test di un Cloud privato basato sulla protezione dei dati con crittografia (Python, modulo Fernet)


Uno studio condotto sulla crittografia per la creazione di un cloud, orientato alla privacy dei contenuti, scritto in Python. Nello specifico:
BackEnd: Modulo Fernet
FrontEnd: Streamlit


# UTILIZZO
Dopo aver scaricato la repository possiamo lanciare da terminale il comando: "streamlit run main.py --server.headless true"

![Alt text](https://github.com/Algorytmo/Crypt/blob/90168af6db5b96927c4cf0b9568c49b4a288bd5b/sceenshot/cmd.jpg?raw=true "cmd")

Incollando su browser l'URL nel terminale, comparirà la schermata di registrazione/login:

![Alt text](https://github.com/Algorytmo/Crypt/blob/90168af6db5b96927c4cf0b9568c49b4a288bd5b/sceenshot/homepage.jpg?raw=true "homepage")

La registrazione non richiede l'utilizzo di una email (al momento), basterà creare una user e una password alfanumerica da almeno 12 caratteri, come ad esempio:

![Alt text](https://github.com/Algorytmo/Crypt/blob/90168af6db5b96927c4cf0b9568c49b4a288bd5b/sceenshot/signup.jpg?raw=true "signup")

Premendo il tasto "Sign-Up":
- Viene generata una chiave NON presente sul server, da salvare personalmente. Servirà per cifrare e decifrare i propri file;
- Viene generata una chiave presente nel server, salvata nella cartella "key", in un file con lo stesso nome della user utilizzata in fase di registrazione;
- Vengono creati i campi "user":"password" dove la password è cifrata tramite il file personale presente nella cartella "key";
- Viene creata, nella cartella "usr", una sottocartella con lo stesso nome della user, che verrà popolata dai file in upload.

![Alt text](https://github.com/Algorytmo/Crypt/blob/90168af6db5b96927c4cf0b9568c49b4a288bd5b/sceenshot/signup-after.jpg?raw=true "signup-after")

Una volta effettuato il login, sarà possibile visualizzare la schermata di:
- Upload:
Sarà possibile caricare uno o più file cifrandoli con la chiave ottenuta in fase di registrazione;

- Download:
Sarà possibile scaricare uno o più file contenuti nel cloud, che verranno decifrati e zippati;

- Elimina file:
Verranno eliminati dal cloud i file selezionati;

- Elimina account:
L'account e tutti i dati collegati ad esso verranno eliminati, file inclusi.
Per riutilizzare il tutto ex-novo, bisognerà effettuare nuovamente la registrazione. 


#ATTENZIONE!
È già presente un account di prova; le credenziali sono:
User: Test
Pwd: 1234567890!@
Token personale: A4JF6nBOKHUq_x7DrESOxzwb8a4kwmmWZNeBHhyQPtU=
Questi dati sono presenti nel file "test_keys.txt"



#AGGIORNAMENTI FUTURI
- Protezione db;
- Protezione key;
