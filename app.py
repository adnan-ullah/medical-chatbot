

from get_Data import bot_response


# FLASK PORTION



from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Adnan , You did a great OFFICE!"


@app.route('/bot', methods=["GET", "POST"])
def response():
    userData = ""
    if request.method == "POST":
        query = request.form
        
        text = query['query']
        bot_reply = bot_response(text)

        if bot_reply[1][0]=="":
          print(bot_reply[0])
          userData = ""

        elif bot_reply[1][0] != "Result" and bot_reply[1]!="":
            result = bot_reply[1][0]
            userData = userData + text

        elif bot_reply[1][0] == "Result":
           
            resultData = bot_response(userData)
            result = resultData[0]
            userData = ''

        bot_reply = bot_response(query['query'])
        result = bot_reply

        return jsonify({"response": result})
    else:
        return "Waiting for BOT"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)