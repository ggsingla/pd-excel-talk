import pandas as pd
import streamlit as st

def load_and_process_file():
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        return df 
    else:
        return None, None, None

def display_data_preview(df):
    st.write("### Data Preview")
    st.dataframe(df)  # Display the first few rows of the DataFrame