import streamlit as st
from streamlit_gsheets import GSheetsConnection
import matplotlib.pyplot as plt
import pandas as pd

@st.cache_resource
def init_connection():
    return st.connection("gsheets", type=GSheetsConnection)

conn = init_connection()


class GoogleSheetData:
    
    @st.cache_data
    def Get_Data(_self,sheet_url, sheet_name):
        try:
            if sheet_url != "" and sheet_name !="":
                df = conn.read(
                    spreadsheet = sheet_url,
                    worksheet= sheet_name,
                    ttl="10m",
                )
                return df
            else:
                return ""
        except Exception as e:
            st.error(e)

    def View(_self):
        col1,col2 = st.columns(2)
        with col1:
            sheet_url = st.text_input(label="Spreadsheet URL")
        with col2:
            sheet_name = st.text_input("Enter Sheet Name")
        df = _self.Get_Data(sheet_url,sheet_name)
        st.write(df)


class FileLinkData:

    @st.cache_data
    def Get_Data(_self, link):
        pass
    
    def View(_self):

        url = st.text_input("Enter file url")

def Offline_View_Data():
    pass

def FileLink_View_Data():
    pass


def Starting_Content():
    choice = st.selectbox("Choose an Option To Connect To Dataset",
                          ("Google Sheets", "File Link",'Upload From Device'))
    if choice =="Google Sheets":
        data = GoogleSheetData()
        data.View()



    