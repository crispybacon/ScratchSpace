from flask import Flask, render_template, url_for, redirect, flash, request, session
from models import db, User
from forms import SignupForm, LoginForm
from flask.ext.sqlalchemy import SQLAlchemy
import socket

app = Flask(__name__)

app.secret_key = '12ff9a90818fe6ebe152a67cf052dfd6f09485ed07fa32aec9349cdcc6157642'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/learningflask'
#db = SQLAlchemy(app)

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
    if 'email' in session:
        return redirect(url_for('home'))
    form = SignupForm()
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('signup.html', form=form)
        else:
            newuser = User(form.firstname.data, form.lastname.data, form.email.data, form.password.data)
            db.session.add(newuser)
            db.session.commit()
            session['email'] = newuser.email
            return redirect(url_for('home'))
    elif request.method == 'GET':
        return render_template('signup.html', form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    if 'email' in session:
        return redirect(url_for('home'))
    form = LoginForm()
    if request.method == "POST":
        if form.validate == False:
            return render_template("login.html", form=form)
        else:
            email = form.email.data
            password = form.password.data
            user = User.query.filter_by(email=email).first()
            if user is not None and user.check_password(password):
                session['email'] = form.email.data
                return redirect(url_for('home'))
            else:
                return redirect(url_for('about'))
    elif request.method == 'GET':
        return render_template('login.html', form=form)

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    session.pop('email', None)
    return redirect(url_for('index'))

@app.route("/home")
def home():
    if 'email' not in session:
        return redirect(url_for('login'))
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)
    #app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', None)
