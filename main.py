import streamlit as st
import signupcheck
import homepage


def logform():
    try:
        with st.sidebar:
            with st.form("Startpage", clear_on_submit = True):
                
                #Sezione Sign-Up
                st.header('Sign-Up')
                user = st.text_input('Scegli il tuo user ID')
                reg_pwd = st.text_input('Scegli la tua password' , placeholder='min. 12 caratteri alfanumerici', type="password").encode(encoding='UTF-8') # converto in byte per poi cifrarlo
                signup = st.form_submit_button('Sign-Up')
                if signup:
                    signupcheck.check(user, reg_pwd)
                
                #Sezione Log-In
                st.header('Login')
                user = st.text_input('User ID')
                pwd = st.text_input('Password', type="password")
                login = st.form_submit_button('Login')
                if login:
                    signupcheck.login(user, pwd)
    
    except FileNotFoundError:
        st.info("Effettua la registrazione")

if __name__ == "__main__":
    logform()
    homepage.homepage()