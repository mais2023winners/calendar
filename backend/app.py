from flask import Flask, request
from chat import ConnectToGPT


app = Flask(__name__)


@app.route("/Ask_GPT", methods=["POST"])
def Ask_GPT():
    print(request.json)
    userMessage = request.json.get(
        "userMessage"
    )  # this should be handeled by React, I do not know how it looks like haha
    response = ConnectToGPT(
        userMessage
    )  # plz ensure that the person working on chat.py is handling the response properly ...
    return response


if __name__ == "__main__":
    app.run(port=8000, debug=True)
