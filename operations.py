from cryptography.fernet import Fernet
import streamlit as st
import os
import sqlite3



def file_encrypt(secret, uploaded_files, savepath, uppedfile):
    mytoken = Fernet(secret)
    for uploaded_file in uploaded_files:
        fname = uploaded_file.name
        with open(os.path.join(savepath,fname), "wb") as file:
            mydata = mytoken.encrypt(bytes(uploaded_file.getbuffer()))
            file.write(mydata)
            uppedfile.append(fname)

def file_decrypt(downsecret, downoption, savepath, vaultpath):
    downtoken = Fernet(downsecret)
    for y in downoption:
        with open(os.path.join(savepath, y), 'rb') as file:
            data = file.read()  
            data = downtoken.decrypt(bytes(data)) #convert data to bytes
        with open(os.path.join(vaultpath, f"{y}"), 'wb') as decfile:
            decfile.write(data)

def dbdel():
    conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), r"db\usr.sqlite3"))
    c = conn.cursor()
    usrcheck = str(c.execute("SELECT userid FROM cred WHERE userid = ?", [str(st.session_state.user)]).fetchone())
    if usrcheck != "None" and usrcheck.lower() != "None":
        c.execute('DELETE FROM cred WHERE userid = ?', [str(st.session_state.user)]) #elimina il campo db
        conn.commit()
        conn.close()
    else:
        pass

def cleardown():
    st.session_state.download = []
    return