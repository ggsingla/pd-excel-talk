import streamlit as st
import re
import io
import contextlib
from src.ai import get_ai_response, get_history


def display_ai_chat(df):
       
    form = st.form(key="ai-chat-form", clear_on_submit=True, border=True)

    with form: 
        prompt = st.text_area("Ask the AI a question related to your data", height=100, key="prompt")
        submitted = st.form_submit_button("Ask")
    if submitted:
        on_submit(prompt, df)
    st.write("Chat History:")
    history = get_history()
    history.reverse()
    history = history[2:] # Skip the first two messages
    for message in history:
        role = "AI" if message.role == "model" else "You"
        st.write(f"{role}:")
        st.write(message.parts[0].text)
        st.divider()

def on_submit(prompt, df):
    response = get_ai_response(prompt)

    st.write("The code that has been generated is:")
    st.code(response, language='python')

    # Extract the Python code from the response
    output_match = re.search(r"```python\n(.*)\n```", response, re.DOTALL)
    if output_match:
        output = output_match.group(1)

        # Capture the output of the exec call
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            try:
                st.write("The code has been executed successfully.")
                st.write("Output:")
                # Execute the generated code with `df` available in the environment
                exec(output, {'df': df, 'st': st})
            except Exception as e:
                st.error(f"Error executing code: {e}")
            output_result = buf.getvalue()

    else:
        st.error("No valid Python code found in the AI response.")