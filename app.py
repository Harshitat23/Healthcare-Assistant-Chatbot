import streamlit as st
from transformers import pipeline
import nltk

chatbot = pipeline("text-generation", model="distilgpt2")

def healthcare_chatbot(user_input):
    if "symptom" in user_input:
        return "Please consult Doctor for accurate advice."
    elif "appointment" in user_input:
        return "Would you like to schedule an appointment with the Doctor?"
    elif "medication" in user_input:
        return "It's important to take prescribed medicine regularly. If you have concerns, consult your doctor."
    else:
        response = chatbot(user_input, max_length=500, num_return_sequences=1)
        return response[0]['generated_text']

def main():
    st.title("Healthcare Assistant Chatbot")
    
    st.markdown("""
        <style>
        .css-1d391kg { 
            background-color: #f0f8ff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        .css-1aumxhk {
            font-size: 20px;
            color: #007bff;
        }
        .css-qj1cim {
            font-size: 18px;
            color: #495057;
        }
        .stButton>button {
            background-color: #007bff;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #0056b3;
        }
        </style>
    """, unsafe_allow_html=True)
    
    user_input = st.text_input("How can I assist you today?", placeholder="Ask your healthcare-related question here...")
    if st.button("Submit"):
        if user_input:
            st.write(f"**User:** {user_input}")
            with st.spinner("Processing your query, please wait..."):
                response = healthcare_chatbot(user_input)
            st.write(f"**Healthcare Assistant:** {response}")
        else:
            st.write("Please enter a message to get a response.")

if __name__ == "__main__":
    main()