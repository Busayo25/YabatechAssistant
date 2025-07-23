import streamlit as st
import pandas as pd
from rapidfuzz import process, fuzz

# Set page config
st.set_page_config(page_title="Yabatech Edubot", page_icon="assets/yabatech_logo.png", layout="centered")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "current_tab" not in st.session_state:
    st.session_state.current_tab = "home"

# Load knowledge base
@st.cache_data
def load_kb():
    url = "https://docs.google.com/spreadsheets/d/1iuMdndmSVkq8JR6Ir42s29-_3QHcGOX6/export?format=csv"
    df = pd.read_csv(url)
    return dict(zip(df['Question'].str.lower(), df['Answer']))

def get_best_match(question, kb, threshold=70):
    questions = list(kb.keys())
    match, score, _ = process.extractOne(question.lower(), questions, scorer=fuzz.token_sort_ratio)
    return kb[match] if score >= threshold else "Hmm 🤔 I'm not sure I understand. Could you rephrase?"

# Create tabs
home_tab, chatbot_tab = st.tabs(['Home', 'Chatbot'])

if st.session_state.current_tab == "home":
    with home_tab:
        st.markdown("### 🎓 Welcome to Yabatech EduBot")
        st.image("assets/yabatech_logo.png", width=200)
        st.subheader("Your Digital Learning Assistant")
        st.write("🚀 Yabatech EduBot helps you with:")
        st.write("- School admissions and processes") 
        st.write("- Course guidance and academic support") 
        st.write("- FAQs about payments, hostels, resumption, etc.") 
        st.write("Just click the button below to start chatting!")
        if st.button("Start Chatbot 💬"):
            st.session_state.current_tab = "chatbot"
elif st.session_state.current_tab == "chatbot":
    with chatbot_tab:
        qa_dict = load_kb()
        col1, col2 = st.columns([1, 12])
        with col1:
            st.image("assets/yabatech_logo.png", width=50)
        with col2:
            st.markdown("<h1 style='padding-top: 5px;'>Yabatech EduBot</h1>", unsafe_allow_html=True)
        st.caption("Ask your question below:")
        user_input = st.text_input("You:", key="user_input", placeholder="Type your question here...")
        if user_input:
            if user_input.lower() == "quit":
                st.session_state.chat_history.append(("You", user_input))
                st.session_state.chat_history.append(("EduBot", "Goodbye! Stay curious! 👋"))
            else:
                reply = get_best_match(user_input, qa_dict)
                st.session_state.chat_history.append(("You", user_input))
                st.session_state.chat_history.append(("EduBot", reply))
        # Chat history display
        for speaker, message in st.session_state.chat_history:
            icon = "🧑" if speaker == "You" else ""
            st.markdown(f"{icon} *{speaker}*: {message}")
        if st.button("🔙 Return Home"):
            st.session_state.current_tab = "home"
            st.session_state.chat_history = []