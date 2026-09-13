from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import sqlite3
import os
from datetime import datetime
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-3.6-flash")
app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("chat_history.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_message TEXT,
        bot_reply TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"]

     # Date & Time feature
    if "date" in user_message.lower() or "time" in user_message.lower():
        now = datetime.now()
        reply = now.strftime("%d-%m-%Y %I:%M:%S %p")
        return jsonify({"reply": reply})

        
    try:
        response = model.generate_content(user_message)
        reply = response.text

        reply = reply.replace("**", "")

        conn = sqlite3.connect("chat_history.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO chats (user_message, bot_reply) VALUES (?, ?)",
            (user_message, reply)
        )

        conn.commit()
        conn.close()

    except Exception as e:
        reply = f"Error: {str(e)}"

    return jsonify({"reply": reply})

@app.route("/history")
def history():

    conn = sqlite3.connect("chat_history.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT user_message, bot_reply FROM chats ORDER BY id DESC"
    )

    chats = cursor.fetchall()

    conn.close()

    return render_template("history.html", chats=chats)


@app.route("/clear_history")
def clear_history():

    conn = sqlite3.connect("chat_history.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM chats")

    conn.commit()
    conn.close()

    return "Chat History Cleared! <a href='/'>Back to Chat</a>"


if __name__ == "__main__":
    app.run(debug=True)