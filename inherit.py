from flask import Flask, redirect, url_for, render_template

#inheritance in flask

app = Flask(__name__)

@app.route('/inheritance')
def inherit():
    return render_template('child.html')

if __name__ == "__main__":
    app.run(debug=True)