import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Retrieve API key from .env
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Check if the API key is loaded
if not GEMINI_API_KEY:
    st.error("API Key not found. Make sure you have a .env file with GEMINI_API_KEY set.")

# Configure the Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Streamlit App
st.title("🔍 AI Code Explainer")
st.write("Enter a code snippet below, and the AI will explain it in simple terms.")

# Code Input
code_input = st.text_area("Paste your code here:", height=300)

# Generate Explanation
if st.button("Explain Code") and code_input:
    try:
        # Use the latest Gemini model
        model = genai.GenerativeModel("gemini-1.5-pro-latest")

        # Generate Explanation
        response = model.generate_content(f"Explain the following code in simple terms:\n{code_input}")

        # Display Explanation
        if response and hasattr(response, 'text'):
            st.write("### 📜 Explanation:")
            st.write(response.text)
        else:
            st.error("Error: No explanation received.")
    except Exception as e:
        st.error(f"Error: {e}")
