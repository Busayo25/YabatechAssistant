import streamlit as st # it is to have an interface
import pandas as pd
from rapidfuzz import process, fuzz # we used nltk before but rapidfuzz is more robust 

home_tab, chatbot_tab = st.tabs(['Home Tab','Chatbot Tab'])

with home_tab:
    def welcome_page():
        st.markdown("### 🎓 Welcome to Yabatech EduBot")
        st.image("assets/yabatech_logo.png", width=200)
        st.subheader("Your Digital Learning Assistant")
        st.markdown("""
            🚀 *Yabatech EduBot helps you with:*
            - School admissions and processes  
            - Course guidance and academic support  
            - FAQs about payments, hostels, resumption, etc.  
            
            Just click the button below to start chatting!
        """)
        if st.button("Start Chatbot 💬"):
            st.session_state.page = "chatbot"
            st.rerun()
        if st.button("🔙 Return Home"):
            st.session_state.page = "welcome"
            st.rerun()

with chatbot_tab:
    st.set_page_config(page_title="Yabatech Edubot", page_icon = "assets/yabatech_logo.png", layout = "centered")
    
    if "page" not in st.session_state:
        st.session_state.page = "welcome"
    if "page" not in st.session_state:
        st.session_state.page = "welcome"
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [] 
    
    @st.cache_data
    def load_kb():
        url = "https://docs.google.com/spreadsheets/d/1iuMdndmSVkq8JR6Ir42s29-_3QHcGOX6/export?format=csv"
        df = pd.read_csv(url)
        return dict(zip(df['Question'].str.lower(), df['Answer']))
    
    def get_best_match(question, kb, threshold=70):
        questions = list(kb.keys())
        match, score, _ = process.extractOne(question.lower(), questions, scorer=fuzz.token_sort_ratio)
        return kb[match] if score >= threshold else "Hmm 🤔 I'm not sure I understand. Could you rephrase?"
    
    
            
    def chatbot_page():
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
    
        
            
    if st.session_state.page == "welcome":
        welcome_page()
    else:
        chatbot_page()