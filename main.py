import streamlit as st
from datetime import datetime
from chat_request import send_openai_request
from horoscope_generator import generate_horoscope

st.set_page_config(page_title="Vedic Astrology App", page_icon="🔮")

st.title("🔮 Vedic Astrology Horoscope Generator")

# Input for date, time, and place of birth
col1, col2 = st.columns(2)
with col1:
    birth_date = st.date_input("Date of Birth")
with col2:
    birth_time = st.time_input("Time of Birth")

place_of_birth = st.text_input("Place of Birth")

if st.button("Generate Horoscope"):
    birth_datetime = datetime.combine(birth_date, birth_time)
    horoscope = generate_horoscope(birth_datetime, place_of_birth)
    st.subheader("Your Vedic Astrology Horoscope")
    st.write(horoscope)

st.subheader("Ask a question about your horoscope")
user_question = st.text_input("Enter your question:")

if st.button("Get Answer"):
    if user_question:
        context = f"Based on the Vedic astrology horoscope for a person born on {birth_date} at {birth_time} in {place_of_birth}, answer the following question: {user_question}"
        answer = send_openai_request(context)
        st.write("Answer:", answer)
    else:
        st.warning("Please enter a question.")

st.markdown("---")
st.markdown("📌 Note: This app uses AI to generate horoscopes and answers. The information provided should be taken as entertainment and not as professional astrological advice.")
