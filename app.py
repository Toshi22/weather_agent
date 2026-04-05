import streamlit as st
from agent import agent

st.set_page_config(page_title="Weather Agent", page_icon="🌦️")

st.title("🌦️ AI Weather Agent")

query = st.text_input("Ask about weather (e.g., 'What's the weather in Kathmandu?')")

if st.button("Ask"):
    if query:
        with st.spinner("Thinking..."):
            response_dict = agent.run(query)
            
            response = response_dict
            
        st.success(response)