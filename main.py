import streamlit as st
from streamlit_option_menu import option_menu
from multiclass_image_classifier import app
from home import Home
from login import LoginForm
from DataViewer import Starting_Content



def main():
    with st.sidebar:
        selected = option_menu(
            menu_title="Main Menu",
            options=['Home', 'Sheet', 'Opt2'],
        )
    if selected == 'Home':
        Home()
    elif selected == 'Sheet':
        Starting_Content()
    else:
        app()



#if "isLoggedIn" not in st.session_state:
#    LoginForm()
#else:
#    if st.session_state['isLoggedIn']:
#        main()
#    else:
#        LoginForm()

main()
            


