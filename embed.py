from flask import Flask, redirect, url_for, render_template

#embedding python code in html known as jinja, which can be viewed in embed.html file

app = Flask(__name__)

@app.route('/tables/<int:n>')
def tables(n):
    return render_template('embed.html', num1=n)

if __name__ == "__main__":
    app.run(debug=True)