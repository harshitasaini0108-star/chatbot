# 🤖 AI ChatBot

An AI-powered chatbot built with Flask, Google Gemini AI, SQLite, HTML, CSS, and JavaScript.

## 🚀 Features

- 🤖 Gemini AI Integration
- 💬 Real-time Chat Interface
- 📜 Chat History Storage
- ⌨️ Enter Key Support
- 🌙 Modern ChatGPT-style Dark UI
- 🗄️ SQLite Database
- 📱 Responsive Design

## 🛠️ Technologies Used

- Python
- Flask
- Google Gemini AI
- SQLite
- HTML
- CSS
- JavaScript
- Bootstrap 5

## 📂 Project Structure

```
chatbot/
│
├── app.py
├── check_models.py
├── .gitignore
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   └── history.html
│
└── chat_history.db
```

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/harshitasaini0108-star/chatbot.git
cd chatbot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install flask
pip install google-generativeai
pip install python-dotenv
```

### 5. Create .env File

```env
GEMINI_API_KEY=YOUR_API_KEY
```

### 6. Run Project

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

## 📜 Chat History

All conversations are stored in SQLite database and can be viewed from:

```
/history
```

## 🎯 Current Version

### AI ChatBot v2.0

- Gemini AI Responses
- Chat History
- Modern UI
- Database Storage
- Date & Time Support

## 👩‍💻 Author

Harshita Saini

GitHub:
https://github.com/harshitasaini0108-star

---
⭐ If you like this project, give it a star on GitHub.
