from flask import Flask, request
from chat import ConnectToGPT
from flask_cors import CORS
import requests
import json

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


@app.route("/google-redirect", methods=["POST"])
def google_login():
    url = "https://oauth2.googleapis.com/token"

    print(request.json)

    payload = (
        "code="
        + request.json.get("code")
        + "&client_id=74963646122-ij1pipmol30cfspvr0q1v9rb40qude2v.apps.googleusercontent.com&client_secret=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&redirect_uri=http%3A%2F%2Flocalhost%3A5173%2Fgoogle-redirect&grant_type=authorization_code"
    )
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    response = requests.request("POST", url, headers=headers, data=payload)

    print(json.loads(response.text))

    return json.loads(response.text)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
