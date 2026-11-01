from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    facts = ["Minecraft", "Roblox", "Fortnite", "Among Us"]
    return random.choice(facts)

app.run(debug=True)