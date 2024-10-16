
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import streamlit as st

#uri = "mongodb+srv://nahid:khan2019@dataset-creator.k4idl.mongodb.net"

# Create a new client and connect to the server
client = MongoClient(st.secrets['mongo']["uri"])

db = client['dtcreate']
collection = db['users']

#collection.insert_one({"_id":0,"name":"nahid"})
#print(collection.count_documents({}))

e = collection.find_one({"Email":"nahidkhan1024bit@gmail.com"})

print(e['Email'])