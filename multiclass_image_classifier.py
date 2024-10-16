import streamlit as st



def app():
    st.title("Select a Label For This Image")
    
    st.image("test.jpg")
    
    genre = st.radio(
        "Select a label for this image",
        ["Comedy", "Drama", "Documentary"],
        
    )
    st.button("Submit", type='primary')
