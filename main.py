from flask import Flask, render_template, url_for, request # pip install flask

flask_app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

