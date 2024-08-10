from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

# Create the model configuration
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

# Initialize the GenerativeModel
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction=(
    "I will provide you with the column names of a CSV file. "
    "You must generate Python code using the pandas library to satisfy the user's {{prompt}}. "
    "You must use the streamlit library to display the output. "
    "Consider that the CSV file is already loaded in a pandas dataframe named `df`."
    "Consider that you have access to the streamlit library as `st` to display the output."
    "No need to provide the explanation or context for the code."
    "No need to load pandas and streamlit libraries"
  ),
)

# Start a new chat session with initial instructions
chat_session = model.start_chat(history=[])

def get_history():
  return chat_session.history

def update_history(prompt):
    chat_session.send_message(prompt)

def get_ai_response(prompt):
    response = chat_session.send_message(prompt)
    return response.text
