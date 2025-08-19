import streamlit as st
from datetime import date, time, datetime
from astro_engine import get_sun_sign, life_path_number, ascendant_bucket, reading_from_profile, answer_question

st.set_page_config(page_title="AI Astrologer (Rule‑Based)", page_icon="🔮", layout="centered")

st.title(" AI Astrologer")
st.caption("For demo purposes only — entertainment, not scientific advice.")

with st.form("birth_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Name", value="Alex")
        dob = st.date_input("Date of Birth", value=date(2000, 1, 1), min_value=date(1900,1,1), max_value=date.today())
    with col2:
        tob = st.time_input("Time of Birth", value=time(12, 0))
        pob = st.text_input("Place of Birth (City, Country)", value="Kolkata, India")

    free_q = st.text_area("Ask one question (career, love, money, studies, health, travel, etc.)", 
                          placeholder="e.g., Will switching jobs this year be good for me?")
    submitted = st.form_submit_button("Get Reading ")

if submitted:
    profile = {
        "name": name.strip() or "Seeker",
        "dob": dob.isoformat(),
        "tob": tob.isoformat(),
        "pob": pob.strip() or "Unknown"
    }
 
    sun = get_sun_sign(dob.month, dob.day)
    life = life_path_number(dob.year, dob.month, dob.day)
    asc = ascendant_bucket(tob)
    st.subheader("Your Birth Snapshot")
    st.write(f"**Name:** {profile['name']}")
    st.write(f"**Sun Sign:** {sun}")
    st.write(f"**Life Path Number:** {life}")
    st.write(f"**Ascendant (approx):** {asc}")
    st.write(f"**Place of Birth:** {profile['pob']}")

    st.divider()
    st.subheader("Personalized Reading")
    reading = reading_from_profile(name=profile['name'], sun_sign=sun, life_path=life, ascendant=asc)
    st.write(reading)

    if free_q:
        st.divider()
        st.subheader("Your Question")
        st.write(f"> {free_q}")
        st.subheader("Response")
        st.write(answer_question(free_q, sun, life, asc))

st.markdown("---")
st.markdown("**Privacy note:** Data stays in your browser session during this demo.")
