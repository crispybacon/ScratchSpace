from flask import Flask, render_template, url_for, redirect, flash

app = Flask(__name__)

app.secret_key = '12ff9a90818fe6ebe152a67cf052dfd6f09485ed07fa32aec9349cdcc6157642'

@app.route("/")
def index():
    flash('Hello World')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
