

from get_Data import bot_response


# FLASK PORTION



from flask import Flask, jsonify, request


def clearingTextFile(textFile):
    with open(textFile, "r+") as myfile:
                myfile.truncate(0)


app = Flask(__name__)
@app.route("/")
def home():
    return "Hello, Adnan , You did a great OFFICE!"


@app.route('/bot', methods=["GET", "POST"])
def response():
    
    
    if request.method == "POST":
        query = request.form
        
        text = query['query']
        bot_reply = bot_response(text)

        if bot_reply[1][0]=="":
            
            clearingTextFile("userGroupQuery.txt")
            
            
            result = bot_reply[0]
          

        elif bot_reply[1][0] != "Result" and bot_reply[1]!="":
            result = bot_reply[1][0]
            with open("userGroupQuery.txt", "a") as myfile:
                myfile.write(text+ " ")


        elif bot_reply[1][0] == "Result":
            data = []
            with open("userGroupQuery.txt", "r") as myfile:
                data = myfile.read().splitlines()
            print(data[0])
            bot_reply = bot_response(data[0])
            result = bot_reply[0]

            clearingTextFile("userGroupQuery.txt")
            


        return jsonify({"response":result})
    else:
        
        return "Waiting for BOT"


if __name__ == "__main__":
    clearingTextFile("userGroupQuery.txt")
    app.run(host="0.0.0.0", port=5000)
  