# 🤖 FRIDAY AI Chatbot 2.0

A sleek, futuristic AI chatbot powered by **Groq's free LLM API** — featuring voice input, memory mode, developer mode, AI tools, and 14 languages.

---

## ✨ Features

- ⚡ 10 Free Groq AI Models (LLaMA, Mixtral, Gemma, DeepSeek, Qwen)
- 🧠 Memory Mode — FRIDAY remembers your preferences
- 🎤 Voice Input — speak your queries
- 💻 Developer Mode — syntax highlighted code blocks
- 🛠 AI Tools — Resume Builder, Email Generator, Code Generator, SQL Builder & more
- 🌐 14 Languages supported
- 🔐 Login system with session management

---

## 🚀 Setup & Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/Friday-Chatbot-2.0.git
cd Friday-Chatbot-2.0
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Get a FREE Groq API Key
- Go to [console.groq.com](https://console.groq.com)
- Click **API Keys → Create API Key**
- Copy your key

### 4. Add your key
- Rename `friday_template.py` to `friday.py`
- Open `friday.py` and find line 14:
```python
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "") or "YOUR_GROQ_KEY_HERE"
```
- Replace `YOUR_GROQ_KEY_HERE` with your actual key

### 5. Run the app
```bash
streamlit run friday.py
```

### 6. Login
```
Username: admin
Password: friday
```

---

## 📁 Project Structure

```
Friday-Chatbot-2.0/
├── friday_template.py   ← rename to friday.py and add your key
├── requirements.txt     ← Python dependencies
└── README.md            ← this file
```

---

## ⚠️ Important

- **Never push `friday.py`** with your real API key to GitHub
- Keep your key private — get a new one at [console.groq.com](https://console.groq.com) if exposed

---

## 🛠 Built With

- [Streamlit](https://streamlit.io) — Python web framework
- [Groq API](https://groq.com) — Free, ultra-fast LLM inference
- Vanilla HTML/CSS/JS — custom futuristic UI

---

*Made with ❤️ by Swaraj Dhumal*