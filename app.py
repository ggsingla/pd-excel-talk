import streamlit as st
from src.data_processing import load_and_process_file, display_data_preview
from src.ai import get_ai_response, update_history
from src.chat_interface import display_ai_chat

st.set_page_config(layout="wide")  # Set the layout to wide for more horizontal space

st.title("AI-Powered Data Analysis")
st.write("AI-powered tool that helps you analyze your data and generate Python code to answer your questions.")

left, right = st.columns([3, 2])


with right:
    right.subheader("Upload and Preview Data")

    try: 
        df = load_and_process_file()
        if df is not None:
            update_history(f"Here are the columns of the CSV file: {df.columns}")
            display_data_preview(df)
        else:
            st.write("Please upload a CSV file to start analyzing.")
    except Exception as e:
        st.write("Please upload a CSV file to start analyzing.")



with left:
    st.subheader("AI Chat")
    if df is not None:
        display_ai_chat(df)
    else:
        st.write("Please upload a CSV file to start asking questions.")
