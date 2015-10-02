from flask import Flask, render_template, url_for, redirect, flash
import socket

app = Flask(__name__)

app.secret_key = '12ff9a90818fe6ebe152a67cf052dfd6f09485ed07fa32aec9349cdcc6157642'

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

if __name__ == '__main__':
    app.run(debug=True)
