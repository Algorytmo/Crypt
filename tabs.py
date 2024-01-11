import streamlit as st
import os
import shutil
import time
import operations



def upload_tab(mypath, usrfolder, filelist):
    uppedfile = []
    with st.form("upload", clear_on_submit=True, border=False):
        uploaded_files = st.file_uploader("SCEGLI I FILE PER L'UPLOAD:", accept_multiple_files=True)
        if uploaded_files is not None:
            savepath = os.path.join(mypath, usrfolder)
            secret = st.text_input("Inserisci la tua chiave personale generata in fase di registrazione")
            upfile = st.form_submit_button("Upload")
            if upfile and secret:
                operations.file_encrypt(secret, uploaded_files, savepath, uppedfile)
        folderfile = os.listdir(savepath)
        for i in folderfile:
            if i not in filelist:
                filelist.append(i)
        for f in uppedfile:
            okup = st.success(f"File {f} caricato con successo")
            time.sleep(1.5)
            okup.empty()
        uppedfile.clear()


def download_tab(mypath, usrfolder, filelist):
    savepath = os.path.join(mypath, usrfolder)
    downoption = st.multiselect('SELEZIONA I TUOI FILE', [x for x in filelist], placeholder="", key="download")
    if downoption:
        downsecret = st.text_input("Inserisci la tua chiave personale generata in fase di registrazione", key="secr")
        on = st.toggle('Conferma il download')
        if on and downsecret:
            os.chdir(savepath)
            os.mkdir(f"{usrfolder}_vault")
            vaultpath = os.path.join(savepath, f"{usrfolder}_vault")
            operations.file_decrypt(downsecret, downoption, savepath, vaultpath)
                #shutil.copy(decr, f"{usrfolder}_vault")
            archived = shutil.make_archive(os.path.join(savepath ,f"{usrfolder}_vault"), 'zip', os.path.join(savepath ,f"{usrfolder}_vault"))
            notify = st.info("File pronti per il download")
            if notify:
                with open(archived, "rb") as file:
                    st.download_button(label="Scarica", data=file, file_name=f'{usrfolder}_vault.zip', mime="application/zip", on_click=operations.cleardown)
                os.remove(archived)
                shutil.rmtree(os.path.join(savepath ,f"{usrfolder}_vault"), ignore_errors=True)


def delete_tab(filelist, mypath, usrfolder):
    with st.form("delete", clear_on_submit=True, border=False):
        folderfile = os.listdir(os.path.join(mypath, usrfolder))
        deloption = st.multiselect('SELEZIONA I TUOI FILE', [x for x in filelist], placeholder="", key="delete")
        delete = st.form_submit_button("Elimina")
        if deloption and delete:
            for y in folderfile:
                if y in filelist:
                    delpath = os.path.join(mypath, usrfolder)
                    os.remove(os.path.join(delpath,y))
                    filelist.remove(y)
                    st.session_state['delete'].remove(y)
                    st.success(f"File {y} eliminato")
                    time.sleep(1.5)
                    if not st.session_state['delete']:
                        st.rerun()


def killtab(mypath, usrfolder):
    savepath = os.path.join(mypath, usrfolder)
    st.warning('ATTENZIONE! TUTTI I TUOI FILE PRESENTI NEL CLOUD SARANNO AUTOMATICAMENTE ELIMINATI')
    kill = st.button(f"ELIMINA ACCOUNT: {str(st.session_state.user)}", type="secondary")
    if kill:
        operations.dbdel()
        shutil.rmtree(savepath, ignore_errors=True)
        killpath = (os.path.join(os.path.dirname(__file__), r'key'))
        killkey = (os.path.join(killpath, f"{str(st.session_state.user)}.fernet"))
        if os.path.isfile(killkey):
            os.remove(killkey)
            if 'user' in st.session_state:
                del st.session_state.user
                st.rerun()
        else:
            pass
