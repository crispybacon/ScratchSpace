from flask import Flask, render_template, url_for, redirect, flash, request
from models import db
from forms import SignupForm
import socket

app = Flask(__name__)

app.secret_key = '12ff9a90818fe6ebe152a67cf052dfd6f09485ed07fa32aec9349cdcc6157642'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/learningflask'

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    #host = socket.gethostbyname(socket.gethostname())
    #name = socket.gethostname()
    #flash(host)
    #flash(name)
    return render_template('about.html')

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if request.method == 'POST':
        return "Success!"
    elif request.method == "GET":
        return render_template('signup.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
