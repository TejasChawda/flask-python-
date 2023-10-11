from flask import Flask, redirect, url_for, render_template

#rendering whole html templates and passing the parameters to the html body

app = Flask(__name__)

@app.route('/<int:n>')
def home(n):
    return render_template('index.html', num1=n)

if __name__ == "__main__":
    app.run(debug=True)