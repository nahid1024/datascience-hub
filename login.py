import streamlit as st
import bcrypt
from pymongo.mongo_client import MongoClient
import bcrypt 


# Hashing the password

@st.cache_resource
def LoginUser(email, passwd):

    client = MongoClient(st.secrets['mongo']["uri"])
    db = client['dtcreate']
    collection = db['users']
    
    if email != "" or passwd != "":
        user_data = collection.find_one({"Email":email})
        if user_data:
            find_pass = user_data['Password']
            is_correct_pass = bcrypt.checkpw(passwd.encode("utf-8"), find_pass)
            if is_correct_pass:
                st.write("Login success")
                st.session_state['isLoggedIn'] = True
                st.rerun()
            else:
                st.error("Incorrect Login Credentials")
        else:
            st.error("User Not Found")

    

def LoginForm():
    with st.form("Form"):
        st.title("Login")
        email = st.text_input("Email", on_change=None, key="email")
        passwd = st.text_input("Password",type='password', on_change=None, key='passwd')

        st.form_submit_button("Submit", type="primary")

    LoginUser(email, passwd)
    