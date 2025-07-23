# 🤖 SmartChatBot – Semantic Chatbot with Streamlit & RapidFuzz

A simple yet intelligent chatbot built using **Pandas**, **Streamlit**, and **RapidFuzz** for semantic matching. This chatbot answers user queries based on pre-defined intents, providing a fast and user-friendly experience through a web interface.

---

## 🚀 Features

- 🔍 **Semantic matching** with RapidFuzz (similarity scoring)
- 🧠 Intent-based logic using a structured `intents.json` or dataset
- 📊 Efficient data handling with Pandas
- 🖥️ Clean and interactive Streamlit web UI
- 💬 Chat-style interface for user interaction
- 🛠️ Easily customizable and extendable

---

## 🧱 Built With

- [Streamlit](https://streamlit.io/) – For building the UI
- [Pandas](https://pandas.pydata.org/) – For data loading and manipulation
- [RapidFuzz](https://github.com/maxbachmann/RapidFuzz) – For fuzzy string matching
- [Python](https://www.python.org/) – Core language

---

## 📸 Demo

![Chatbot UI Demo](screenshot.png)

<img width="1920" height="1080" alt="Screenshot (7)" src="https://github.com/user-attachments/assets/3e19bdb4-1259-4e8f-9a60-ff344450b384" />


## 📁 Project Structure

```bash
├── chatbot.py           # Main Streamlit app
├── intents.csv/json     # Predefined questions and answers
├── utils.py             # (Optional) Helper functions
├── requirements.txt     # Required Python packages
└── README.md            # Project documentation
