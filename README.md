#  AI Astrologer (Internship Demo Project)

This project was built as part of an internship screening assignment.  
The task was to create a simple “AI Astrologer” app that collects user birth details and generates astrology-inspired responses, including answering one free-text question.  

I chose a **rule-based approach** instead of training an ML model because:  
- It’s fast and transparent (no hidden black-box behavior).   
 

##  Features
- Clean UI built with **Streamlit** to collect: **Name, Date of Birth, Time of Birth, Place of Birth**.  
- Generates:  
  - **Sun Sign** (basic Western astrology).  
  - **Life Path Number** (numerology reduction).  
  - **Ascendant Bucket** (time-based segmentation for flavor).  
- Produces a **personalized reading** with unique traits and advice.  
- Handles **one free-text question** (career, love, money, health, study, travel, etc.) via simple keyword intent detection.  
- Runs entirely **locally** with no external API calls → lightweight and reproducible.  

## Quickstart

### 1) Setup
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

### 2) Run
```bash
streamlit run app.py
```
This will open the app in your browser (usually at `http://localhost:8501`).  

##  Demo 
1. Fill the form with a sample user.  
2. Click **Get Reading** → show generated snapshot + personalized reading.  
3. Ask one free-text question (e.g., *"Should I change jobs this year?"*) → show response.  
4. Briefly explain architecture (UI + rule engine).  


##  Project Structure
ai-astrologer/
├── app.py             # Streamlit UI
├── astro_engine.py    # Rule-based astrology logic
├── requirements.txt   # Dependencies
└── README.md          # Documentation

##  Notes & Reflections
- This app is **rule-based**, not a real astrological calculator. It was designed as a **demo project** for internship evaluation.  
- If I had more time, I would extend it with:  
  - A proper birth chart API or astronomical library.  
  - An AI-driven response generator (LLM) for free-text questions.  
  - User data logging and simple dashboards.  
- **Disclaimer:** This project is for entertainment and learning purposes only.  
