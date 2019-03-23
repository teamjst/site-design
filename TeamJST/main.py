from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/userhome")
def userhome():
    return render_template("userhome.html")

@app.route("/lightsetting")
def lightsetting():
    return render_template("lightsetting.html")

@app.route("/sound")
def sound():
    return render_template("sound.html")

@app.route("/timer")
def timer():
    return render_template("timer.html")

@app.route("/addDevice")
def addDevice():
    return render_template("addDevice.html")

import webbrowser

webbrowser.open('http://google.com')


if __name__ == "__main__":
    app.run(debug=True)