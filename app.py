<<<<<<< HEAD

=======
>>>>>>> e7d77cc698137e6ecc290d23afef937a89050e85

from get_Data import bot_response


# FLASK PORTION
<<<<<<< HEAD
=======

from flask import Flask, jsonify, request
>>>>>>> e7d77cc698137e6ecc290d23afef937a89050e85

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Adnan , You did a great OFFICE!"


@app.route('/bot', methods=["GET", "POST"])
def response():
    if request.method == "POST":
        query = request.form
        bot_reply = bot_response(query['query'])
        result = bot_reply

        return jsonify({"response": result})
    else:
        return "Waiting for BOT"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)