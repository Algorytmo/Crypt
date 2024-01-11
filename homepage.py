import streamlit as st
import os
import tabs



def homepage():
    try:
        filelist = []
        usrfolder = (str(st.session_state.user).lower())
        mypath = (os.path.join(os.path.dirname(__file__), r'usr'))
        st.header("PERSONAL VAULT -- Benvenuto %s" % st.session_state.user)
        tab1, tab2, tab3, tab4 = st.tabs(["Upload", "Download", "Elimina", "Rimuovi Account"])

        with tab1:
            tabs.upload_tab(mypath, usrfolder, filelist)
        with tab2:
            tabs.download_tab(mypath, usrfolder, filelist) 
        with tab3:
            tabs.delete_tab(filelist, mypath, usrfolder)
        with tab4:
            tabs.killtab(mypath, usrfolder)
                
    except FileNotFoundError:
        pass          
    except AttributeError:
        pass
    #except ValueError:
    #    pass
    #except UnboundLocalError:
    #    pass


if __name__ == "__main__":
    homepage()