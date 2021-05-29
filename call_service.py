from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/whitelist", methods=['GET', 'POST'])
def whitelist():
    resp = VoiceResponse()
    
    resp.say("You are on our Whitelist!", voice='alice')

    return str(resp)

@app.route("/blacklist", methods=['GET', 'POST'])
def blacklist():
    resp = VoiceResponse()
    resp.say("You are on our blacklist!", voice='alice')

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
