# Flask Website
from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "This is a home page <h1>Welcome !<h1>"
if __name__ == "__main__":
    app.run()
