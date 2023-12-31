from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/loginform', methods=["POST", "GET"])
def form():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template('form.html')

# @app.route('/<usr>')
# def user(usr):
#     return render_template('user.html', userName=usr)

@app.route('/<usr>')
def user(usr):
    return f"<h3>{usr}</h3>"

if __name__ == "__main__":
    app.run(debug=True)
