from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!, my name is tejas</p>"

@app.route("/<name>")
def home(name):
    return f"hello {name}"

@app.route("/admin")
def admin():
    return redirect(url_for("home", name="Admin"))

if __name__ == "__main__":
    app.run(debug=True)

##flask basics


