from flask import Flask
import g4f
app = Flask(__name__)

@app.route('/')
def hello_world():
    response = g4f.ChatCompletion.create(
    model=g4f.models.default,
    messages=[{"role": "user", "content": "how are you"}],
    timeout=120,
    )
    return "RESPONSE: " + str(response)
