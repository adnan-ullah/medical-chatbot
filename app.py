# DETECT PORTION [Author : PCIU__std]


from get_Data import bot_response, findCallName


# FLASK PORTION

from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Adnan , You did a great OFFICE!"


@app.route('/bot', methods=["GET", "POST"])
def response():
    if request.method == "POST":
        query = dict(request.form)['query']
        call_name = findCallName(query)

        checkingCallHime = "%% HUMAN %%"
        bot_reply = bot_response(query)

        if checkingCallHime in bot_reply:

            bot_reply = bot_reply.replace(checkingCallHime, call_name)

        result = bot_reply

        return jsonify({"response": result})
    else:
        return "Waiting for BOT"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
