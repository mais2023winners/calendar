from flask import Flask, request
from chat import ConnectToGPT
from flask_cors import CORS


app = Flask(__name__)

CORS(app, origins=["*"])


@app.route("/Ask_GPT", methods=["POST"])
def Ask_GPT():
    print(request.json)
    userMessage = request.json.get("userMessage")
    userToken = request.json.get("userToken")
    userToken[
        "client_id"
    ] = "74963646122-ij1pipmol30cfspvr0q1v9rb40qude2v.apps.googleusercontent.com"
    userToken["client_secret"] = "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"
    # this should be handeled by React, I do not know how it looks like haha
    response = ConnectToGPT(
        userMessage, userToken, request.json.get("history")
    )  # plz ensure that the person working on chat.py is handling the response properly ...
    return response


if __name__ == "__main__":
    app.run(port=8000, debug=True)
