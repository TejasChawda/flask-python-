from flask import Flask, redirect, url_for, render_template

#embedding python code in html known as jinja, which can be viewed in embed.html file

app = Flask(__name__)

@app.route('/colleagues')
def colleagues():
    return render_template('list.html', emps=["ajay","roshan","sharath","amogh","baganna","priyanshu","hemanth","akshay","al-fareed","soumya"])

if __name__ == "__main__":
    app.run(debug=True)