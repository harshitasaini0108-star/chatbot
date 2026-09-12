from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"].lower()

    if "hello" in user_message:
        reply = "Hello! How can I help you?"

    elif "python" in user_message:
        reply = "Python is a powerful programming language."

    elif "bye" in user_message:
        reply = "Goodbye!"

    else:
        reply = "I am still learning."

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)