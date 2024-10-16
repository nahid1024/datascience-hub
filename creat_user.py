from pymongo.mongo_client import MongoClient
import streamlit as st
import bcrypt

client = MongoClient(st.secrets['mongo']["uri"])

db = client['dtcreate']
collection = db['users']

name = input("Enter Name: ")
email = input("Enter Email: ")
password = input("Enter password: ").encode("utf-8")

salt = bcrypt.gensalt()

hashed = bcrypt.hashpw(password,salt)
user_id = collection.count_documents({})+1
user = {
    "_id":user_id,
    "Name": name,
    "Email": email,
    "Password": hashed

}
collection.insert_one(user)

