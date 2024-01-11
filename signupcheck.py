from cryptography.fernet import Fernet
import streamlit as st
import pandas as pd
import sqlite3
import os



def check(user, reg_pwd):
    special_characters = ("1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "0" , "!" , "@" , "#" , "$" , "?")
    forbidden_characters = ("%", "^" , "&" , "*" , "(" , ")" , "-" , "+" , "_" , "=" , "," , "<" , ">", "/", "'")

    conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), r"db\usr.sqlite3"))
    c = conn.cursor()
    usrcheck = str(c.execute("SELECT userid FROM cred WHERE userid = ?", [user]).fetchone()).lstrip("('").strip("',)") # check nel db se user id già preso
    pwdspok = any(i for i in reg_pwd.decode(encoding='utf-8') if i in special_characters) # check se la pwd contiene caratteri speciali consentiti
    pwdspnok = any(i for i in reg_pwd.decode(encoding='utf-8') if i in forbidden_characters) # check se la pwd contiene caratteri speciali non consentiti
    pwdlen = len(reg_pwd.decode(encoding='utf-8')) # check lunghezza pwd - min 12
    if usrcheck != "None" and usrcheck.lower() != "None":
        st.error('Username ' + user + ' non disponibile')
    elif pwdlen < 12:
        st.error("Password troppo corta! Si prega di usarne una almeno da 12 caratteri alfanumerici")
    elif pwdspok == False:
        st.error('La password deve contenere caratteri speciali')
    elif pwdspnok == True:
        st.error('La password non può contenere caratteri proibiti')
    else:
        signup(user, reg_pwd, c, conn)


def signup(user, reg_pwd, c, conn):
    KEY = Fernet.generate_key()
    with open(os.path.join(os.path.dirname(__file__), r'key\%s.fernet' % (user)), 'ab+') as file:
        file.write(KEY)
    with open(os.path.join(os.path.dirname(__file__), r'key\%s.fernet' % (user)), 'rb') as sec:
        key = sec.read()
    pers = Fernet(key)
    keypwd = pers.encrypt(reg_pwd) # cifra la password
    x = {"userid":[user],
        "password":[keypwd]}
    df = pd.DataFrame(x, columns= ['userid','password'])
    c.execute('CREATE TABLE IF NOT EXISTS cred (userid, password)') # crea i campi del db
    conn.commit()
    df.to_sql('cred', conn, if_exists='append', index=False)
    conn.close()
    dirname = user.lower()
    parent_dir = (os.path.join(os.path.dirname(__file__), r'usr'))
    path = os.path.join(parent_dir, dirname)
    os.mkdir(path)
    perskey = Fernet.generate_key()
    st.markdown('ATTENZIONE! Ecco la tua chiave personale:')
    st.info(f'{perskey.decode()}')
    st.markdown('Se la perdi i tuoi file saranno irrecuperabili!')
    st.success('Benvenuto ' + user + '. Ora puoi effettuare il login')


def login(user, pwd):
    conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), r"db\usr.sqlite3"))
    c = conn.cursor()
    checkId = str(c.execute("SELECT userid FROM cred WHERE userid = ?", [user]).fetchone()).lstrip("('").strip("',)") # check nel db se user esiste
    if checkId == user:
        pswDb = str(c.execute("SELECT password FROM cred WHERE userid = ?", [checkId]).fetchone()).lstrip("('").strip("',)").strip("b'") # check nel db la pwd e la confronta con quella inserita nel login
        with open(os.path.join(os.path.dirname(__file__), r'key\%s.fernet' % (checkId)), 'rb') as secret:
            line = secret.read()
            pers = Fernet(line)
            control = pers.decrypt(pswDb.encode(encoding='utf-8'))
        passwd = control.decode(encoding='utf-8') 
        if pwd == passwd:
            c.close()
            conn.close()
            if user not in st.session_state: # definisco l'oggetto user nella sessione, altrimenti streamlit cancella tutto ad ogni update di widget
                st.session_state.user = user             
        else:
            st.error('Password errata')
    else:
        st.error("Username non corretto")